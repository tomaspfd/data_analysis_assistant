#!/usr/bin/env python
from pydantic import BaseModel, Field
import pandas as pd
from crewai.flow import Flow, listen, start
from typing import List, Dict, Any

from .crews.a_data_processing_crew.data_processing_crew import DataProcessingCrew
from .crews.b_data_exploring_crew.data_exploring_crew import DataExploringCrew
from .crews.c_data_cleaning_crew.data_cleaning_crew import DataCleaningCrew
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




class DataCleaningState(BaseModel):
    csv_path: str = ""
    data_profiling_report: str = ""
    dataset_overview: str = ""
    columns: List[str] = Field(default_factory=list)
    sample_rows: List[Dict[str, Any]] = Field(default_factory=list)
    nova_path: str = ""
    reports_path: str = ""
    cleaned_datasets_path: str = ""

class DataCleaningFlow(Flow[DataCleaningState]):

    @start()
    def dataset_overview_crew(self):

        if not self.state.csv_path:
            raise ValueError("csv_path is empty in DataCleaningState")

        current_file = Path(__file__).resolve()
        NOVA_ROOT = find_nova_root(current_file, "NOVA")
        self.state.nova_path = str(NOVA_ROOT)
        REPORTS_DIR = NOVA_ROOT / "reports"
        CLEANED_DIR = NOVA_ROOT / "cleaned_datasets"
        os.makedirs(REPORTS_DIR, exist_ok=True)
        os.makedirs(CLEANED_DIR, exist_ok=True)
        self.state.reports_path = str(REPORTS_DIR)
        self.state.cleaned_datasets_path = str(CLEANED_DIR)

        # --- Your deterministic data extraction step here ---
        try:
            df = pd.read_csv(self.state.csv_path)
            self.state.columns = df.columns.tolist()
            self.state.sample_rows = df.head().to_dict(orient="records")
        except Exception as e:
            self.state.columns = []
            self.state.sample_rows = []
            print(f"Error loading CSV: {e}")

        # --- Now pass ONLY what you want to the research agent ---
        result = (
            DataProcessingCrew()
            .crew()
            .kickoff(
                inputs={
                    "columns": self.state.columns,
                    "sample_rows": self.state.sample_rows,
                    "csv_file_path": self.state.csv_path,
                }
            )
        )



        # When reading/writing:
        reports_dir = Path(self.state.reports_path)

        dataset_overview_path = reports_dir / "dataset_overview.md"
        data_profiling_report_path = reports_dir / "data_profiling_report.md"

        dataset_overview = ""
        if dataset_overview_path.exists():
            with open(dataset_overview_path, "r", encoding="utf-8") as f:
                dataset_overview = f.read()

        data_profiling_report = ""
        if data_profiling_report_path.exists():
            with open(data_profiling_report_path, "r", encoding="utf-8") as f:
                data_profiling_report = f.read()

        self.state.data_profiling_report = data_profiling_report
        self.state.dataset_overview = dataset_overview



    @listen("dataset_overview_crew")
    def run_exploring_crew(self):


        # Now, run the exploring crew with all needed inputs!
        exploring_result = (
            DataExploringCrew()
            .crew()
            .kickoff(
                inputs={
                    "columns": self.state.columns,
                    "sample_rows": self.state.sample_rows,
                    "csv_file_path": self.state.csv_path,  
                    "data_profiling_report": self.state.data_profiling_report,
                    "reports_dir": self.state.reports_path,
                }
            )
        )



    @listen("run_exploring_crew")
    def run_cleaning_crew(self):


        reports_dir = Path(self.state.reports_path)

        # FIX: join with Path(...)
        numerical_cleaning_plan_path = reports_dir / "numerical_cleaning_plan.md"
        categorical_cleaning_plan_path = reports_dir / "categorical_cleaning_plan.md"
        integrity_cleaning_plan_path  = reports_dir / "integrity_cleaning_plan.md"

        numerical_cleaning_plan = ""
        if numerical_cleaning_plan_path.exists():
            with open(numerical_cleaning_plan_path, "r", encoding="utf-8") as f:
                numerical_cleaning_plan = f.read()

        categorical_cleaning_plan = ""
        if categorical_cleaning_plan_path.exists():
            with open(categorical_cleaning_plan_path, "r", encoding="utf-8") as f:
                categorical_cleaning_plan = f.read()

        integrity_cleaning_plan = ""
        if integrity_cleaning_plan_path.exists():
            with open(integrity_cleaning_plan_path, "r", encoding="utf-8") as f:
                integrity_cleaning_plan = f.read()

        # Now, run the cleaning crew with all needed inputs!
        cleaning_result = (
            DataCleaningCrew()
            .crew()
            .kickoff(
                inputs={
                    "columns": self.state.columns,
                    "sample_rows": self.state.sample_rows,
                    "csv_file_path": self.state.csv_path,  
                    "data_profiling_report": self.state.data_profiling_report,
                    "numerical_cleaning_plan": numerical_cleaning_plan,
                    "categorical_cleaning_plan": categorical_cleaning_plan,
                    "integrity_cleaning_plan": integrity_cleaning_plan,
                    "reports_dir": self.state.reports_path,
                    "cleaned_dir": self.state.cleaned_datasets_path,
                }
            )
        )



        



def kickoff():
    # Demo inputs - replace with your actual user inputs or CLI args
    flow = DataCleaningFlow()
    #flow.state.csv_path = "C:/Users/tomas/Desktop/Internship Daniel/Coding/CSV_Analysis v2/electric_vehicles_spec_2025.csv"
    flow.kickoff()



def plot():
    flow = DataCleaningFlow()
    flow.plot()


if __name__ == "__main__":

    kickoff()
