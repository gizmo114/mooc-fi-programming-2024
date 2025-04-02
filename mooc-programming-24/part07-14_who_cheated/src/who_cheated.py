import csv
from datetime import datetime, timedelta


def cheaters() -> list:
    students_time = {}
    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            students_time[line[0]] = datetime.strptime(line[1], "%H:%M") + timedelta(
                hours=3
            )
    cheaters = []
    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            if (datetime.strptime(line[3], "%H:%M") > students_time[line[0]]) and line[0] not in cheaters:
                cheaters.append(line[0])
    return cheaters

