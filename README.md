## CSV Analysis Workflow

**NOVA** is an agentic data-analysis pipeline that takes you from a raw CSV to a polished, insight-rich report, automatically. It runs in two major flows: a **CSV Cleaning Flow** that profiles, diagnoses, and cleans the data; and an **Answering Flow** that plans and executes an analysis to answer a user’s question with tables, figures, and narrative. A [Streamlit](https://streamlit.io/) UI ties it all together so you can upload a CSV, let the agents work, and then ask questions interactively. The orchestration of agents is powered by [CrewAI](https://github.com/joaomdmoura/crewai).

---

### Flow 1 — CSV Cleaning Flow (3 crews, 15 agents)

#### 1) Data Processing Crew (2 agents)
- **Data Research Agent**  
  Receives the dataset’s **column names** and a few **sample rows** to infer domain/industry context. It performs targeted **online research** to situate the dataset in its broader landscape (terminology, conventions, typical metrics, etc.).
- **Data Profiling Agent** *(with Code Interpreter)*  
  Uses Python to compute **summary statistics** for numeric columns, **value distributions** for categorical columns, **missingness**, and **type mismatches**. It merges these findings with the research and writes a **baseline profiling report**, including a **one-sentence description for each column**.

#### 2) Data Exploring Crew (9 agents; all with Code Interpreter)
- **Numerical Diagnostics (3 agents)**
  - Two independent **diagnostic agents** scan *all* numeric columns to flag **every anomaly** (outliers, impossible values, inconsistent scales, etc.).
  - A **numerical cleaning planner** consolidates their outputs into a detailed, executable **numerical cleaning plan**.
- **Categorical Diagnostics (3 agents)**
  - Mirrors the numerical flow for **categorical columns** (invalid categories, inconsistent labels, rare/unexpected values, etc.), producing a **categorical cleaning plan**.
- **Integrity Diagnostics (3 agents)**
  - Focuses on **dataset-wide integrity**: missing values, duplicates, key consistency, cross-column rules—producing an **integrity cleaning plan**.

#### 3) Data Cleaning Crew (4 agents; all with Code Interpreter)
- **Numerical Cleaning Agent**, **Categorical Cleaning Agent**, **Integrity Cleaning Agent**  
  Each receives its respective plan and **implements it deterministically**. Cleaners:
  - **Pass forward both** a **cleaning report** (what changed, why) **and** the **updated dataset**, so subsequent cleaners operate on the **latest version** (preventing rework or conflicts).
- **Cleaning Summary Agent**  
  Consolidates the three cleaning reports into a **final cleaning summary**.
  
**Outputs of Flow 1**
- A full set of **reports** (profiling, diagnostics, plans, and final cleaning summary).
- A **clean dataset** (e.g., `cleaned_data_three.csv`).

---

### Flow 2 — Answering Flow (1 crew, 3 agents)

#### Prompt Answering Crew
- **Answering Plan Agent**  
  Consumes the **profiling report**, **final cleaning summary**, and the **user’s prompt** (plus columns & sample rows) and produces a **deterministic, step-by-step plan**.  
  The plan explicitly selects whether to use the **original dataset**, the **cleaned dataset**, or **both**, and specifies concrete I/O (figure filenames, optional table CSVs, final markdown).
- **Plan Review Agent**  
  **Edits and finalizes** the plan: checks completeness, feasibility, ordering, and that it fully answers the user’s question with no missing steps.
- **Final Answering Agent** *(with Code Interpreter)*  
  Executes the **reviewed plan exactly**:
  - Generates **figures (PNGs)** and optional **table CSVs**.
  - Writes a polished, self-contained **Markdown report** with embedded figures that **fully answers** the user’s prompt using text, tables, and charts.

**Output of Flow 2**
- `final_answer.md` + referenced figures/tables, ready to share.

---

### Streamlit UI

- **Upload CSV** → automatically runs the **CSV Cleaning Flow**; you get all reports and a clean dataset.
- **Ask a question** in the prompt box → runs the **Answering Flow**; you get a rendered **final Markdown report** (with figures) right in the UI.
- Download buttons are available for generated artifacts. That’s it—upload, clean, ask, and read the answer.




## Installation & Setup

### Prerequisites
- **Python** 3.10+ recommended
- **Node/JS not required**
- (Optional, if you want local models) **[Ollama](https://ollama.com/)** installed and at least one model pulled (e.g. `ollama pull llama3.2` or `ollama pull gemma3`). 

## Environment Variables
- For OpenAI API models (e.g., openai/gpt-4o-2024-11-20): OPENAI_API_KEY=...
- For Google Gemini models (e.g., gemini/gemini-2.5-flash): GEMINI_API_KEY=...
- For the research agent (Serper.dev Google Search API): SERPER_API_KEY=...



## Project Layout 
```
NOVA/
├─ streamlit/
│  └─ CSVBot.py                # Streamlit UI
├─ csv_cleaning_flow/
│  └─ src/csv_cleaning_flow/
│     ├─ main.py               # DataCleaningFlow + state
│     └─ crews/                # Processing, Exploring, Cleaning crews
├─ answering_flow/
│  └─ src/answering_flow/
│     ├─ main.py               # DataAnsweringFlow + state
│     └─ crews/                # Prompt Answering crew (plan, review, execute)
├─ reports/                    # profiling + exploring + cleaning outputs (created at runtime)
├─ cleaned_datasets/           # cleaned CSV(s) (created at runtime)
├─ answering_reports/          # final_answer.md + figures (created at runtime)
├─ uploads/                    # user-uploaded CSVs (created at runtime)
└─ model_config.txt            # 2-line model selector written by the UI
```

## Run WebApp
```
streamlit run NOVA/streamlit/CSVBot.py
```