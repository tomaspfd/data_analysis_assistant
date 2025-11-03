from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Optional, Tuple
from crewai_tools import (
    CodeInterpreterTool
)
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()
from functools import lru_cache


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


current_file = Path(__file__).resolve()
NOVA_ROOT = find_nova_root(current_file, "NOVA")






# def _read_model_config(cfg_path: Optional[Path] = None) -> Tuple[str, str]:
#     """
#     Reads model_config.txt (2 lines):
#       line 1: model source -> 'Local' or 'API'
#       line 2: selection:
#         - if source == 'Local': a local model tag (e.g., 'llama3.2')
#         - if source == 'API':  'provider/model' (e.g., 'gemini/gemini-2.5-flash', 'openai/gpt-4o-2024-08-06')

#     Returns (source_normalized, selection_raw).
#     Falls back to ('API', 'gemini/gemini-2.5-flash') if missing/malformed.
#     """
#     path = cfg_path or MODEL_CFG
#     try:
#         lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
#         source = (lines[0] if len(lines) >= 1 else "API").strip()
#         selection = (lines[1] if len(lines) >= 2 else "gemini/gemini-2.5-flash").strip()
#     except Exception:
#         source, selection = "API", "gemini/gemini-2.5-flash"

#     # normalize source
#     src = source.lower()
#     if src not in {"local", "api"}:
#         src = "api"
#     source_norm = "Local" if src == "local" else "API"
#     return source_norm, selection


# def resolve_llm_from_config(temperature: float = 0.2,
#                             cfg_path: Optional[Path] = None) -> Tuple[str, str, LLM]:
#     """
#     Single entry point:
#       - reads model source & selection
#       - constructs a CrewAI LLM
#       - returns (source, normalized_model, llm)

#     Normalization rules:
#       - Local  -> provider forced to 'ollama', model = 'ollama/<local_tag>'
#       - API    -> expects 'provider/model'; normalized to '<provider>/<model>'
#                  Supports: openai (OPENAI_API_KEY), gemini (GEMINI_API_KEY).
#                  Other providers fall back to '<provider>/<model>' and try ENV
#                  '<PROVIDER>_API_KEY' if present.

#     Raises a clear error if needed API keys are missing.
#     """
#     source, selection = _read_model_config(cfg_path)

#     if source == "Local":
#         # selection is a plain tag like 'llama3.2' or 'gemma3'
#         local_tag = selection.split("/", 1)[-1]  # ignore accidental prefixes
#         model_id = f"ollama/{local_tag}"
#         llm = LLM(model=model_id, temperature=temperature)
#         return source, model_id, llm

#     # API branch: expect 'provider/model'
#     if "/" not in selection:
#         # Be forgiving: default to gemini if provider omitted
#         provider, model_name = "gemini", selection
#     else:
#         provider, model_name = selection.split("/", 1)

#     provider = provider.lower().strip()
#     model_name = model_name.strip()
#     normalized = f"{provider}/{model_name}"

#     if provider == "openai":
#         api_key = os.getenv("OPENAI_API_KEY")
#         if not api_key:
#             raise RuntimeError("OPENAI_API_KEY is not set but 'openai' was selected in model_config.txt.")
#         llm = LLM(model=normalized, api_key=api_key, temperature=temperature)
#         return "API", normalized, llm

#     if provider == "gemini":
#         api_key = os.getenv("GEMINI_API_KEY")
#         if not api_key:
#             raise RuntimeError("GEMINI_API_KEY is not set but 'gemini' was selected in model_config.txt.")
#         llm = LLM(model=normalized, api_key=api_key, temperature=temperature)
#         return "API", normalized, llm

#     # Generic provider fallback (e.g., 'anthropic/claude-3-haiku' if you add it later)
#     maybe_key = os.getenv(f"{provider.upper()}_API_KEY")
#     kwargs = {"temperature": temperature}
#     if maybe_key:
#         kwargs["api_key"] = maybe_key
#     llm = LLM(model=normalized, **kwargs)
#     return "API", normalized, llm




# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class DataCleaningCrew:
    """Data Cleaning Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"





    @property
    def cleaning_llm(self) -> LLM:
        """Build an LLM for deterministic processing (e.g., profiling) using the latest model_config.txt."""
        cfg_path = (NOVA_ROOT / "model_config.txt").resolve()
        # 1) Read config (2 lines: source, selection)
        try:
            lines = [ln.strip() for ln in cfg_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
            source    = (lines[0] if len(lines) >= 1 else "API").strip()
            selection = (lines[1] if len(lines) >= 2 else "gemini/gemini-2.5-flash").strip()
        except Exception:
            source, selection = "API", "gemini/gemini-2.5-flash"

        print(f"\n\n\n\n\n\n[LLM] processing_llm config: source='{source}', selection='{selection}'\n\n\n\n\n\n")
        
        src = source.lower()
        src = src if src in {"local", "api"} else "api"

        # 2) Resolve to a CrewAI LLM
        temperature = 0.1
        if src == "local":
            # Force Ollama for local selections (e.g., 'llama3.2' -> 'ollama/llama3.2')
            tag = selection.split("/", 1)[-1]
            model_id = f"ollama/{tag}"
            print(f"[LLM] processing_llm -> {model_id}")
            return LLM(model=model_id, temperature=temperature)

        # API branch: expect 'provider/model'
        if "/" not in selection:
            provider, model_name = "gemini", selection
        else:
            provider, model_name = selection.split("/", 1)

        provider = provider.lower().strip()
        model_id = f"{provider}/{model_name.strip()}"

        # Map provider to env var key if known
        env_keys = {
            "openai": "OPENAI_API_KEY",
            "gemini": "GEMINI_API_KEY",
        }
        #kwargs = {"temperature": temperature, "additional_drop_params": ["stop"]}
        kwargs = {"temperature": temperature}
        api_env = env_keys.get(provider, f"{provider.upper()}_API_KEY")
        api_key = os.getenv(api_env)
        if api_key:
            kwargs["api_key"] = api_key
        elif provider in env_keys:
            raise RuntimeError(f"{api_env} is not set but '{provider}' was selected in model_config.txt.")

        print(f"[LLM] processing_llm -> {model_id}")
        return LLM(model=model_id, **kwargs)






    @property
    def summarizing_llm(self) -> LLM:
        """Build an LLM for deterministic processing (e.g., profiling) using the latest model_config.txt."""
        cfg_path = (NOVA_ROOT / "model_config.txt").resolve()
        # 1) Read config (2 lines: source, selection)
        try:
            lines = [ln.strip() for ln in cfg_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
            source    = (lines[0] if len(lines) >= 1 else "API").strip()
            selection = (lines[1] if len(lines) >= 2 else "gemini/gemini-2.5-flash").strip()
        except Exception:
            source, selection = "API", "gemini/gemini-2.5-flash"

        src = source.lower()
        src = src if src in {"local", "api"} else "api"

        # 2) Resolve to a CrewAI LLM
        temperature = 0.2
        if src == "local":
            # Force Ollama for local selections (e.g., 'llama3.2' -> 'ollama/llama3.2')
            tag = selection.split("/", 1)[-1]
            model_id = f"ollama/{tag}"
            print(f"[LLM] processing_llm -> {model_id}")
            return LLM(model=model_id, temperature=temperature)

        # API branch: expect 'provider/model'
        if "/" not in selection:
            provider, model_name = "gemini", selection
        else:
            provider, model_name = selection.split("/", 1)

        provider = provider.lower().strip()
        model_id = f"{provider}/{model_name.strip()}"

        # Map provider to env var key if known
        env_keys = {
            "openai": "OPENAI_API_KEY",
            "gemini": "GEMINI_API_KEY",
        }
        #kwargs = {"temperature": temperature, "additional_drop_params": ["stop"]}
        kwargs = {"temperature": temperature}
        api_env = env_keys.get(provider, f"{provider.upper()}_API_KEY")
        api_key = os.getenv(api_env)
        if api_key:
            kwargs["api_key"] = api_key
        elif provider in env_keys:
            raise RuntimeError(f"{api_env} is not set but '{provider}' was selected in model_config.txt.")

        print(f"[LLM] processing_llm -> {model_id}")
        return LLM(model=model_id, **kwargs)






    # If you would lik to add tools to your crew, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def numerical_cleaning_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["numerical_cleaning_agent"],  # type: ignore[index]
            verbose=True,
            llm=self.cleaning_llm,
            memory=True,
            tools=[CodeInterpreterTool(unsafe_mode=True)]  # type: ignore[index]
        )
    
    @agent
    def categorical_cleaning_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["categorical_cleaning_agent"],  # type: ignore[index]
            verbose=True,
            llm=self.cleaning_llm,
            memory=True,
            tools=[CodeInterpreterTool(unsafe_mode=True)]  # type: ignore[index]
        )
    

    @agent
    def integral_cleaning_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["integral_cleaning_agent"],  # type: ignore[index]
            verbose=True,
            llm=self.cleaning_llm,
            memory=True,
            tools=[CodeInterpreterTool(unsafe_mode=True)]  # type: ignore[index]
        )



    @agent
    def cleaning_reporting_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["cleaning_reporting_agent"],  # type: ignore[index]
            verbose=True,
            llm=self.summarizing_llm,
            memory=True,
            tools=[CodeInterpreterTool(unsafe_mode=True)]  # type: ignore[index]
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    @task
    def numerical_cleaning_task(self) -> Task:
        return Task(
            config=self.tasks_config["numerical_cleaning_task"],  # type: ignore[index]
            output_file=str(NOVA_ROOT / "reports" / "numerical_cleaning_report.md")
        )

    @task
    def categorical_cleaning_task(self) -> Task:
        return Task(
            config=self.tasks_config["categorical_cleaning_task"],  # type: ignore[index]
            output_file=str(NOVA_ROOT / "reports" / "categorical_cleaning_report.md")
        )
    
    @task
    def integral_cleaning_task(self) -> Task:
        return Task(
            config=self.tasks_config["integral_cleaning_task"],  # type: ignore[index]
            output_file=str(NOVA_ROOT / "reports" / "integral_cleaning_report.md")
        )
    

    @task
    def cleaning_reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["cleaning_reporting_task"],  # type: ignore[index]
            output_file=str(NOVA_ROOT / "reports" / "summary_cleaning_report.md")
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Data Cleaning Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
