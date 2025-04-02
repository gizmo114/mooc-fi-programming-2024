import csv
from datetime import datetime, timedelta


def final_points() -> dict:
    students_time = {}
    students_points = {}
    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            students_time[line[0]] = datetime.strptime(line[1], "%H:%M") + timedelta(
                hours=3
            )
            students_points[line[0]] = {}

    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            if students_time[line[0]] > datetime.strptime(line[3], "%H:%M"):
                if line[1] not in students_points[line[0]]:
                    students_points[line[0]][line[1]] = int(line[2])
                elif students_points[line[0]][line[1]] < int(line[2]):
                    students_points[line[0]][line[1]] = int(line[2])

    total_points = {}
    for name, data in students_points.items():
        total_points[name] = 0
        for exercise, points in data.items():
            total_points[name] += points

    return total_points
