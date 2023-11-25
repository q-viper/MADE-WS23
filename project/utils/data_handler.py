import pandas as pd
import os
from pathlib import Path
from typing import Union
import re, demoji

from .configs import Config, DataSource, DataType


class DataHandler:
    def __init__(self, config: Config):
        self.config = config

    def __read_csv(self, path: Union[str, Path]) -> pd.DataFrame:
        df = pd.read_csv(path, sep=self.config.csv_sep)
        return df

    def __load_data(self, path: Union[str, Path]) -> pd.DataFrame:
        if self.config.data_type == DataType.CSV:
            return self.__read_csv(path)
        else:
            raise NotImplementedError(f"Not implemented for {self.config.data_type}")

    def load_data(self) -> "DataHandler":
        if self.config.data_source == DataSource.LOCAL:
            self.data = self.__load_data(
                self.config.local_data_path / self.config.data_file_name
            )
        elif self.config.data_source == DataSource.REMOTE:
            self.data = self.__read_csv(self.config.remote_data_path)
            if self.config.save_remote_data and self.config.data_type == DataType.CSV:
                self.data.to_csv(
                    self.config.local_data_path / self.config.data_file_name
                )
        elif self.config.data_source == DataSource.KAGGLE:
            import json

            with open(self.config.credentials_path) as f:
                kaggle_auth = json.load(f)
                os.environ["KAGGLE_USERNAME"] = kaggle_auth["username"]
                os.environ["KAGGLE_KEY"] = kaggle_auth["key"]

            import kaggle

            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(
                self.config.kaggle_dataset_name,
                path=self.config.local_data_path,
                unzip=True,
            )
            self.data = self.__load_data(
                self.config.local_data_path / self.config.data_file_name
            )
        else:
            raise NotImplementedError(f"Not implemented for {self.config.data_source}")
        return self

    def drop_columns(self, columns: list) -> "DataHandler":
        self.data = self.data.drop(columns=columns)
        return self

    def drop_rows(self, keep_condition: Union[str, callable]) -> "DataHandler":
        if isinstance(keep_condition, str):
            self.data = self.data.query(keep_condition)
        else:
            self.data = self.data[self.data.apply(keep_condition, axis=1)]
        return self

    def apply(
        self, column: str, func: callable, new_column: str = None
    ) -> "DataHandler":
        if new_column is not None:
            self.data[new_column] = self.data[column].apply(func)
        else:
            self.data[column] = self.data[column].apply(func)
        return self

    def __clean_text(self, text: str) -> str:
        text = re.sub(r"http\S+", "", text)  # remove links
        text = re.sub(r"@\S+", "", text)  # remove mentions
        text = re.sub(r"#\S+", "", text)  # remove hashtags
        text = re.sub(r"RT", "", text)  # remove retweets

        text = demoji.replace(text, "")  # remove emojis
        return text

    def clean_data(self) -> "DataHandler":
        if self.config.focus_columns:
            self.data = self.data[self.config.focus_columns]
        if self.config.drop_duplicates:
            self.data = self.data.drop_duplicates()
        if self.config.drop_na:
            self.data = self.data.dropna()
        if self.config.clean_text_column:
            for col in self.config.clean_text_column:
                self.data[col] = self.data[col].apply(self.__clean_text)
        if self.config.filter_date:
            if self.config.date_column in self.data.columns:
                self.data[self.config.date_column] = pd.to_datetime(
                    self.data[self.config.date_column]
                )
                pass
            else:
                raise ValueError("Date column not match.")
            if self.config.min_date:
                self.data = self.data[
                    self.data[self.config.date_column]
                    >= pd.to_datetime(self.config.min_date)
                ]
            if self.config.max_date:
                self.data = self.data[
                    self.data[self.config.date_column]
                    <= pd.to_datetime(self.config.max_date)
                ]

        return self


if __name__ == "__main__":
    config = Config(data_source=DataSource.LOCAL)
    tweet_data = DataHandler(config).load_data().clean_data()
    print(tweet_data.data.head())

    covid_cols = [
        "iso_code",
        "continent",
        "location",
        "date",
        "total_cases",
        "new_cases",
        "new_deaths",
        "total_deaths",
        "new_vaccinations",
        "total_vaccinations",
        "total_tests",
        "new_tests",
        "hosp_patients",
    ]
    config = Config(
        data_source=DataSource.LOCAL,
        data_file_name="owid-covid-data.csv",
        focus_columns=covid_cols,
        filter_date=True,
    )
    covid_data = DataHandler(config).load_data().clean_data()
    print(covid_data.data.head())
