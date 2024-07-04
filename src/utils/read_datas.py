import csv
import os
import queue

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def read_csv(file_name: str) -> list:
    file_path = rf'{os.path.join(BASE_PATH, "testdatas", file_name)}'  # windows /t會被轉
    datas: list = []
    with open(file_path, "r", newline='', encoding='utf-8') as csv_file:
        # data = csv_file.read()
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            datas.append(row)
    return datas


if __name__ == "__main__":
    # print(BASE_PATH)
    datas = read_csv("qa01.csv")
    # print(type(datas))
    user_data_queue = queue.Queue()
    user_data_queue.put_nowait(datas)
    for data in datas:
        user_data_queue.put_nowait(data)

    for _ in range(10):
        print(user_data_queue.get())

    # print(os.path.join(BASE_PATH, "testdatas"))
