from project.pipeline import Pipeline
from project.utils.configs import Config

from sqlalchemy import create_engine
import pandas as pd
import os


def test_pipeline():
    # pipeline = Pipeline()
    # pipeline.run()
    config = Config()

    print("Checkin DB Files...")
    covid_db = config.local_data_path / "covid.db"
    tweet_db = config.local_data_path / "tweet.db"

    if not os.path.exists(covid_db):
        raise Exception("COVID Database not found")
    if not os.path.exists(tweet_db):
        raise Exception("Tweet Database not found")

    engine1 = create_engine(f"sqlite:///{str(covid_db)}", echo=True)
    engine2 = create_engine(f"sqlite:///{str(tweet_db)}", echo=True)

    covid_data = pd.read_sql_table("covid", con=engine1)
    tweet_data = pd.read_sql_table("tweet", con=engine2)

    if covid_data.empty:
        raise Exception("COVID Database is empty")
    if tweet_data.empty:
        raise Exception("Tweet Database is empty")

    print("Done.")


if __name__ == "__main__":
    test_pipeline()
