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





# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class PromptAnsweringCrew:
    """Prompt Answering Crew"""


    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"





    @property
    def answering_llm(self) -> LLM:
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
        temperature = 0.4
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
    def answering_plan_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["answering_plan_agent"],  # type: ignore[index]
            verbose=True,
            llm=self.answering_llm,
            memory=True,
            allow_delegation=False,
            #tools=[CodeInterpreterTool(unsafe_mode=True)]  # type: ignore[index]
        )
    
    @agent
    def plan_review_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["plan_review_agent"],  # type: ignore[index]
            verbose=True,
            llm=self.answering_llm,
            memory=True,
            allow_delegation=False,
            #tools=[CodeInterpreterTool(unsafe_mode=True)]  # type: ignore[index]
        )
    
    @agent
    def final_answering_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["final_answering_agent"],  # type: ignore[index]
            verbose=True,
            llm=self.answering_llm,
            memory=True,
            allow_delegation=False,
            tools=[CodeInterpreterTool(unsafe_mode=True)]  # type: ignore[index]
        )
    




    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    


    @task
    def answering_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config["answering_plan_task"],  # type: ignore[index]
            output_file=str(NOVA_ROOT / "answering_reports" / "answering_plan.md")
        )
    
    @task
    def plan_review_task(self) -> Task:
        return Task(
            config=self.tasks_config["plan_review_task"],  # type: ignore[index]
            output_file=str(NOVA_ROOT / "answering_reports" / "final_reviewed_plan.md")
        )

    @task
    def final_answering_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_answering_task"],  # type: ignore[index]
            #output_file=str(NOVA_ROOT / "final_answer.md")
        )
    


    @crew
    def crew(self) -> Crew:
        """Creates the Prompt Answering Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
