#!/usr/bin/env python
from pydantic import BaseModel, Field
import pandas as pd
from crewai.flow import Flow, listen, start
from typing import List, Dict, Any


from .crews.a_prompt_answering_crew.prompt_answering_crew import PromptAnsweringCrew
import os
from pathlib import Path
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





class DataAnsweringState(BaseModel):
    user_prompt: str = ""
    csv_path: str = ""
    columns: List[str] = Field(default_factory=list)
    sample_rows: List[Dict[str, Any]] = Field(default_factory=list)
    conversation_history: List[Dict[str, Any]] = Field(default_factory=list)
    nova_path: str = ""
    reports_path: str = ""
    cleaned_datasets_path: str = ""
    answering_reports_path: str = ""


class DataAnsweringFlow(Flow[DataAnsweringState]):

    @start()
    def run_answering_crew(self):

        current_file = Path(__file__).resolve()
        NOVA_ROOT = find_nova_root(current_file, "NOVA")
        self.state.nova_path = str(NOVA_ROOT)
        REPORTS_DIR = NOVA_ROOT / "reports"
        CLEANED_DIR = NOVA_ROOT / "cleaned_datasets"
        self.state.reports_path = str(REPORTS_DIR)
        self.state.cleaned_datasets_path = str(CLEANED_DIR)
        ANSWERING_DIR = NOVA_ROOT / "answering_reports"
        os.makedirs(ANSWERING_DIR, exist_ok=True)
        self.state.answering_reports_path = str(ANSWERING_DIR)

        # --- Your deterministic data extraction step here ---
        try:
            df = pd.read_csv(self.state.csv_path)
            self.state.columns = df.columns.tolist()
            self.state.sample_rows = df.head().to_dict(orient="records")
        except Exception as e:
            self.state.columns = []
            self.state.sample_rows = []
            print(f"Error loading CSV: {e}")



        # When reading/writing:
        reports_dir = REPORTS_DIR

        dataset_overview_path = reports_dir / "dataset_overview.md"
        data_profiling_report_path = reports_dir / "data_profiling_report.md"
        summary_cleaning_path = reports_dir / "summary_cleaning_report.md"  # make sure your consolidator writes this

        dataset_overview = ""
        if dataset_overview_path.exists():
            with open(dataset_overview_path, "r", encoding="utf-8") as f:
                dataset_overview = f.read()

        data_profiling_report = ""
        if data_profiling_report_path.exists():
            with open(data_profiling_report_path, "r", encoding="utf-8") as f:
                data_profiling_report = f.read()
        
        summary_cleaning_report = ""
        if summary_cleaning_path.exists():
            with open(summary_cleaning_path, "r", encoding="utf-8") as f:
                summary_cleaning_report = f.read()


        # Now, run the cleaning crew with all needed inputs!
        final_answer = (
            PromptAnsweringCrew()
            .crew()
            .kickoff(
                inputs={
                    "user_prompt": self.state.user_prompt,
                    "columns": self.state.columns,
                    "sample_rows": self.state.sample_rows,
                    "csv_file_path": self.state.csv_path,  
                    "data_profiling_report": data_profiling_report,
                    "dataset_overview": dataset_overview,
                    "summary_cleaning_report": summary_cleaning_report,
                    "cleaned_dir": self.state.cleaned_datasets_path,
                    "answering_reports_dir": self.state.answering_reports_path,
                }
            )
        )







        



def kickoff():
    # Demo inputs - replace with your actual user inputs or CLI args
    flow = DataAnsweringFlow()
    #flow.state.user_prompt = "What is the distribution of the cargo volume of the cars in the dataset?"
    #flow.state.csv_path = "C:/Users/tomas/Desktop/Internship Daniel/Coding/CSV_Analysis v2/electric_vehicles_spec_2025.csv"
    flow.kickoff()



def plot():
    flow = DataAnsweringFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
