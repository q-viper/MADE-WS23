import sys
import os
import pandas as pd
from sqlalchemy import create_engine

sys.path.append(os.getcwd())
from project.utils.data_handler import DataHandler
from project.utils.configs import Config, DataSource

config = Config(
    remote_data_path="https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV",
    data_source=DataSource.REMOTE,
    data_file_name="D_Bahnhof_2020_alle.CSV",
    csv_sep=";",
)


def valid_ioft(row: pd.Series) -> bool:
    x = row["IFOPT"]
    if isinstance(x, float):
        return False
    chunks = x.split(":")

    if len(chunks) == 3:
        return len(chunks[0]) == 2 and chunks[1].isdigit() and chunks[2].isdigit()
    else:
        return (
            len(chunks[0]) == 2
            and chunks[1].isdigit()
            and chunks[2].isdigit()
            and chunks[3].isdigit()
        )


data = (
    DataHandler(config)
    .load_data()
    .drop_columns(["Status"])
    .drop_rows(keep_condition="Verkehr in ['FV', 'RV', 'nur DPN']")
    .apply("Breite", lambda x: float(x.replace(",", ".")))
    .apply("Laenge", lambda x: float(x.replace(",", ".")))
    .drop_rows(keep_condition="-90<Laenge and Laenge<90 and -90<Breite and Breite<90")
    .drop_rows(keep_condition=valid_ioft)
    .drop_rows(
        keep_condition="Verkehr != '' and EVA_NR !='' and DS100 != '' and NAME != '' and Verkehr != '' and Laenge != '' and Breite != '' and Betreiber_Name != '' and Betreiber_Nr != ''"
    )
)

engine = create_engine("sqlite:///./data/trainstops.db", echo=True)
data.data.to_sql("trainstops", con=engine, if_exists="replace")
print("Done.")

print(data.data.head())