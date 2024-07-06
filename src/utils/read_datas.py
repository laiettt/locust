import csv
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parents[2]
TESTDATA_FOLDER = "testdatas"


def read_csv(file_name: str) -> list:
    file_path = BASE_PATH / TESTDATA_FOLDER / file_name
    datas: list = []
    with open(file_path, "r", newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            datas.append(row)
    return datas
