import streamlit as st
# use "streamlit run main.py" to run this file

import sys
from pathlib import Path
import os
from functools import lru_cache
import re
from datetime import datetime




# ----------------------------
# Helpers
# ----------------------------
@lru_cache(maxsize=1)
def find_nova_root(start: Path | None = None, folder_name: str = "NOVA") -> Path:
    """
    Walk upward from `start` (or this file) to locate the folder named `folder_name`.
    - Case-insensitive match on the directory name (supports 'NOVA' vs 'Nova').
    - Respects the NOVA_ROOT environment variable if set and valid.
    - Raises RuntimeError if not found.
    """
    if start is None:
        start = Path(__file__).resolve()
    # Ensure we start from a directory, not a file
    if start.is_file():
        start = start.parent


    # 1) Environment variable override (nice for tests/packaging)
    env_root = os.getenv("NOVA_ROOT")
    if env_root:
        p = Path(env_root).expanduser().resolve()
        if p.is_dir() and p.name.lower() == folder_name.lower():
            return p

    # 2) Walk upward until we hit folder_name
    p = start
    for _ in range(20):  # depth guard
        if p.name.lower() == folder_name.lower():
            return p
        # If you're ever running from a sibling, also allow a child named NOVA at this level
        candidate = (p / folder_name)
        if candidate.is_dir():
            return candidate.resolve()
        if p.parent == p:
            break
        p = p.parent

    # 3) Last-chance scan ancestors by name
    for anc in start.parents:
        if anc.name.lower() == folder_name.lower():
            return anc

    raise RuntimeError(f"Could not locate '{folder_name}' above {start}")

NOVA_ROOT     = find_nova_root(Path(__file__).resolve(), "NOVA")
REPORTS_DIR   = NOVA_ROOT / "reports"
UPLOADS_DIR   = NOVA_ROOT / "uploads"
CLEANED_DIR   = NOVA_ROOT / "cleaned_datasets"
ANSWERING_DIR = NOVA_ROOT / "answering_reports"
MODEL_CFG     = NOVA_ROOT / "model_config.txt"


# Point to the `NOVA` directory
sys.path.append(str(NOVA_ROOT))

# Import your flows & states
from csv_cleaning_flow.src.csv_cleaning_flow.main import DataCleaningFlow, DataCleaningState
from answering_flow.src.answering_flow.main import DataAnsweringFlow, DataAnsweringState


def write_model_config_to_file(model_source: str, model_name: str):
    try:
        MODEL_CFG.write_text(f"{model_source}\n{model_name}")
    except Exception as e:
        st.warning(f"Could not persist model config: {e}")




# For markdown box
def render_final_answer_box():
    md_path = ANSWERING_DIR / "final_answer.md"
    st.markdown("---")
    st.subheader("📝 Final Answer (live preview)")

    cols = st.columns([1, 1, 3])
    with cols[0]:
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()
    with cols[1]:
        if md_path.exists():
            st.download_button(
                "⬇️ Download",
                data=md_path.read_text(encoding="utf-8"),
                file_name="final_answer.md",
                mime="text/markdown",
                use_container_width=True
            )

    if not md_path.exists():
        st.info("No `final_answer.md` yet. Ask a question above and run the answering flow.")
        return

    # Show last modified time
    mtime = datetime.fromtimestamp(md_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    st.caption(f"Last updated: {mtime}")

    # Read markdown
    text = md_path.read_text(encoding="utf-8")

    # --- Extract image refs like ![alt](fig_01.png) ---
    img_refs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)

    # Remove image tags from the markdown so we don't show broken inline images
    text_without_imgs = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)

    # Render the text part
    st.markdown(text_without_imgs)

    # Render figures below using Streamlit so local files display correctly
    shown_any = False
    for rel in img_refs:
        img_path = (ANSWERING_DIR / rel).resolve()
        if img_path.exists():
            if not shown_any:
                st.markdown("#### Figures")
                shown_any = True
            st.image(str(img_path), caption=rel)
        else:
            st.warning(f"Referenced image not found: {rel}")

    # Optional: help debug what's in the folder
    with st.expander("🧩 Debug: files in answering_reports"):
        files = sorted(p.name for p in ANSWERING_DIR.glob("*"))
        st.write(files)


# ----------------------------
# Streamlit Page
# ----------------------------
st.set_page_config(page_title="CSV Analysis Assistant", page_icon="📊")

# Inject CSS (kept your styling)
st.markdown("""
<style>
/* Layout spacing */
div.block-container {
  padding-left: 1rem !important;
  padding-right: 1rem !important;
  padding-top: 0rem !important;
  max-width: 100% !important;
}
section.main > div {
  padding-left: 0 !important;
  padding-right: 0 !important;
}

/* Typography */
body, .stTextArea textarea {
  font-family: 'Segoe UI', sans-serif;
  font-size: 16px;
}

/* Chat: add subtle spacing between bubbles */
.stChatMessage {
  margin-bottom: 0.5rem;
}

/* Optional: nicer buttons */
.stButton > button {
  border-radius: 12px;
  padding: 0.5rem 0.9rem;
}

/* Optional: expander header weight */
.streamlit-expanderHeader {
  font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------
# Session State Init
# ----------------------------
if "model_source" not in st.session_state:
    st.session_state.model_source = "Local"
if "selected_model" not in st.session_state:
    st.session_state.selected_model = "gemma3"

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
    st.session_state.conversation_history_full = []

# Session State Init (add this near the others)
if "last_upload_fingerprint" not in st.session_state:
    st.session_state.last_upload_fingerprint = None

# Cleaning flow artifacts/state
if "original_csv_path" not in st.session_state:
    st.session_state.original_csv_path = None
if "cleaned_csv_path" not in st.session_state:
    st.session_state.cleaned_csv_path = None
if "profiling_report_path" not in st.session_state:
    st.session_state.profiling_report_path = None
if "cleaning_report_path" not in st.session_state:
    st.session_state.cleaning_report_path = None

# Flows stored once in session
if "cleaning_flow" not in st.session_state:
    st.session_state.cleaning_flow = None
if "answering_flow" not in st.session_state:
    st.session_state.answering_flow = None

# ----------------------------
# Actions
# ----------------------------
def run_cleaning_flow_immediately(csv_bytes, filename: str):
    st.session_state.conversation_history = []
    st.session_state.conversation_history_full = []
    uploads_dir = UPLOADS_DIR
    uploads_dir.mkdir(parents=True, exist_ok=True)
    saved_path = uploads_dir / (filename or "uploaded.csv")
    with open(saved_path, "wb") as f:
        f.write(csv_bytes if isinstance(csv_bytes, (bytes, bytearray)) else bytes(csv_bytes))

    st.session_state.original_csv_path = str(saved_path)

    st.session_state.cleaning_flow = DataCleaningFlow()

    st.session_state.cleaning_flow.state.csv_path = str(saved_path)

    with st.spinner("Running dataset research, profiling, exploration, and cleaning..."):
        try:
            st.session_state.cleaning_flow.kickoff()
        except Exception as e:
            st.error(f"Cleaning flow failed: {e}")
            return

    # Optional chat notice
    st.session_state.conversation_history_full.append(
        {"role": "assistant", "content": "✅ CSV uploaded and cleaned. Reports saved in /reports."}
    )

    st.toast("Cleaning flow completed!")



if "busy" not in st.session_state: st.session_state.busy = False

def send_and_clear():

    if st.session_state.busy: return
    st.session_state.busy = True

    try:

        if not st.session_state.original_csv_path:
            st.session_state.conversation_history_full.append(
                {"role": "assistant", "content": "⚠️ Please upload a CSV first."}
            )
            st.session_state.input = ""
            return

        reports_dir = REPORTS_DIR
        required = ["dataset_overview.md", "data_profiling_report.md", "summary_cleaning_report.md"]
        if not all((reports_dir / r).exists() for r in required):
            st.session_state.conversation_history_full.append(
                {"role": "assistant", "content": "⏳ Still preparing reports. Please try again in a moment."}
            )
            st.session_state.input = ""
            return


        user_input = st.session_state.input.strip()
        if not user_input:
            return

        st.session_state.conversation_history.append({"role": "user", "content": user_input})
        st.session_state.conversation_history_full.append({"role": "user", "content": user_input})


        st.session_state.answering_flow = DataAnsweringFlow()
        st.session_state.answering_flow.state.user_prompt = user_input
        st.session_state.answering_flow.state.csv_path = st.session_state.original_csv_path

        with st.spinner("Answering your question..."):
            try:
                st.session_state.answering_flow.kickoff()
            except Exception as e:
                st.exception(e)
                return

        # Your answering flow doesn’t expose a final text field; it writes to answering_reports/.
        # If your PromptAnsweringCrew returns text into state, display it; else confirm completion.
        ans_state = st.session_state.answering_flow.state
        maybe_text = getattr(ans_state, "final_markdown", None) or getattr(ans_state, "answer_markdown", None)
        if maybe_text:
            st.session_state.conversation_history_full.append({"role": "assistant", "content": maybe_text})
        else:
            st.session_state.conversation_history_full.append(
                {"role": "assistant", "content": "✅ Answer generated. Check /answering_reports for the markdown file."}
            )

        st.session_state.input = ""



    finally:
        st.session_state.busy = False



# ----------------------------
# Layout
# ----------------------------
left_col, right_col = st.columns([0.5, 3.5])

with left_col:
    st.markdown("### Settings")
    st.selectbox("Model Source", ["Local", "API"], key="model_source")
    if st.session_state.model_source == "Local":
        st.selectbox("Local Model", ["gemma3", "llama3.2", "granite3-dense"], key="selected_model")
    else:
        st.selectbox("API Model", ["gemini/gemini-2.5-flash", "gemini/gemini-2.5-pro", "gemini/gemini-2.0-flash", "gemini/gemini-1.5-flash", "openai/gpt-4o-2024-11-20", "openai/gpt-4.1-nano-2025-04-14", "openai/o4-mini-2025-04-16"], key="selected_model")

    write_model_config_to_file(st.session_state.model_source, st.session_state.selected_model)


    st.markdown("### Data")

    # --- replace your upload handling block ---
    uploaded_csv = st.file_uploader("Upload CSV file", type=["csv"], key="csv_upload")
    if uploaded_csv is not None:
        # fingerprint: name + size (fast and good enough)
        try:
            buf = uploaded_csv.getbuffer()
            fingerprint = f"{uploaded_csv.name}:{len(buf)}"
        except Exception:
            fingerprint = uploaded_csv.name

        if st.session_state.last_upload_fingerprint != fingerprint:
            st.session_state.last_upload_fingerprint = fingerprint
            #run_cleaning_flow_immediately(buf, uploaded_csv.name)  # pass bytes buffer directly


    st.markdown("### Actions")
    if st.button("🧹 Clear Chat"):
        st.session_state.conversation_history = []
        st.session_state.conversation_history_full = []
        st.toast("Chat history cleared!")


    with st.expander("Artifacts"):
        for rel in ["reports/dataset_overview.md", "reports/data_profiling_report.md",
                    "reports/summary_cleaning_report.md", "answering_reports/final_answer.md"]:
            p = NOVA_ROOT / rel
            if p.exists():
                with open(p, "rb") as f:
                    st.download_button(f"Download {rel}", f, file_name=Path(rel).name)

with right_col:
    st.title("📊 CSV Analysis Assistant")

    for entry in st.session_state.conversation_history_full:
        role = entry["role"]
        with st.chat_message("user" if role == "user" else "assistant"):
            # render as markdown; Streamlit safely ignores raw HTML by default
            st.markdown(str(entry["content"]))


    # Bottom input
    with st.container():
        st.markdown('<div class="bottom-input-container">', unsafe_allow_html=True)
        col1, col2 = st.columns([5, 1])
        with col1:
            st.text_area(
                label="Message",
                placeholder="Ask a question about your dataset (e.g., 'What is Q4 2024 sales by region?').",
                height=70,
                label_visibility="collapsed",
                key="input",
            )
        with col2:
            st.button("➤", on_click=send_and_clear, key="send_button")
        st.markdown('</div>', unsafe_allow_html=True)



    # Final answer preview box
    render_final_answer_box()

