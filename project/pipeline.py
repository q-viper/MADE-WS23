from pathlib import Path
from sqlalchemy import create_engine

from project.utils.data_handler import DataHandler
from project.utils.configs import Config, DataSource


class Pipeline:
    def __init__(self):
        pass

    def run(self):
        # local_data_path = Path("./data")
        # print(f"Local data path: {local_data_path}")

        config = Config(
            data_source=DataSource.LOCAL,
            # local_data_path=local_data_path,
            clean_text_column=["text"],
        )
        print(f"Loading Twitter data with config: {config}")
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
            # local_data_path=local_data_path,
            data_file_name="owid-covid-data.csv",
            focus_columns=covid_cols,
            filter_date=True,
            drop_na=False,  # some columns have na values and it does not mean that it was missing
        )

        print(f"Loading Covid data with config: {config}")
        covid_data = DataHandler(config).load_data()
        covid_data = covid_data.clean_data()
        print(covid_data.data.head())

        # store df as sqlite databse
        covid_db = config.local_data_path / "covid.db"
        tweet_db = config.local_data_path / "tweet.db"

        print("Storing covid and tweet data as sqlite database.")
        engine = create_engine(f"sqlite:///{str(covid_db)}", echo=True)
        covid_data.data.to_sql("covid", con=engine, if_exists="replace")

        engine = create_engine(f"sqlite:///{str(tweet_db)}", echo=True)
        tweet_data.data.to_sql("tweet", con=engine, if_exists="replace")
        # print(f"Database stored at {local_data_path}")
        print("Done.")


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()
