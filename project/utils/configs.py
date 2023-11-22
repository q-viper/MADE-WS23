from dataclasses import dataclass
from pathlib import Path
from enum import Enum
from typing import Optional, List


class DataSource(Enum):
    LOCAL = "local"
    REMOTE = "remote"
    KAGGLE = "kaggle"


class DataType(Enum):
    CSV = "csv"


@dataclass
class Config:
    credentials_path: Path = Path(__file__).parent.parent / "kaggle.json"
    data_source: DataSource = DataSource.LOCAL
    local_data_path: Path = Path(__file__).parent.parent.parent / "data/"
    remote_data_path: Optional[
        str
    ] = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    save_remote_data: bool = True
    data_file_name: str = "covid19_tweets.csv"
    data_type: DataType = DataType.CSV
    kaggle_dataset_name: str = "gpreda/covid19-tweets"

    # for covid19_tweets.csv:
    # iso_code,continent,location,date,total_cases,new_cases,new_deaths,total_deaths,new_vaccinations,total_vaccinations
    # total_tests, new_tests,hosp_patients
    focus_columns: Optional[List[str]] = None  # if None, all columns are used
    drop_duplicates: bool = True
    drop_na: bool = True
    clean_text_column: Optional[List[str]] = None  # if None, no text column is cleaned

    filter_date: bool = True  # if True, filter data by date
    date_column: Optional[str] = "date"  # if None, no date column is used
    min_date: Optional[str] = "2020-07-25"  # if None, no min date is used
    max_date: Optional[str] = "2020-08-30"  # if None, no max date is used
