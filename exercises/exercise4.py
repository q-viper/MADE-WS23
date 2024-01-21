import pandas as pd
import zipfile
import urllib.request as requests


def download_file_to_path(url, path):
    requests.urlretrieve(url, path)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


URL = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
PATH = "mowesta-dataset-20221107.zip"
download_file_to_path(URL, PATH)


with zipfile.ZipFile(PATH, "r") as zip_ref:
    zip_ref.extractall("mowesta-dataset-20221107")


df = pd.read_csv(
    "./mowesta-dataset-20221107/data.csv",
    delimiter=";",
    decimal=",",
    index_col=False,
    usecols=[
        "Geraet",
        "Hersteller",
        "Model",
        "Monat",
        "Temperatur in °C (DWD)",
        "Batterietemperatur in °C",
        "Geraet aktiv",
    ],
)


df = df.rename(
    columns={
        "Temperatur in °C (DWD)": "Temperatur",
        "Batterietemperatur in °C": "Batterietemperatur",
    }
)


# Convert temperatures to Fahrenheit
df["Temperatur"] = df["Temperatur"].apply(celsius_to_fahrenheit)
df["Batterietemperatur"] = df["Batterietemperatur"].apply(celsius_to_fahrenheit)

# Convert column types
column_types = {
    "Geraet": int,
    "Hersteller": str,
    "Model": str,
    "Monat": int,
    "Temperatur": float,
    "Batterietemperatur": float,
    "Geraet aktiv": str,
}
df = df.astype(column_types)

# Write to SQLite database
df.to_sql(
    "temperatures", "sqlite:///temperatures.sqlite", if_exists="replace", index=False
)
