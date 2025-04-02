import urllib.request
import json
import math


def retrieve_all() -> list:
    request = urllib.request.urlopen(
        "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    )
    courses = json.loads(request.read())
    return_list = []
    for course in courses:
        if course["enabled"]:
            exercise_sum = 0
            for score in course["exercises"]:
                exercise_sum += score
            return_tuple = (
                course["fullName"],
                course["name"],
                course["year"],
                exercise_sum,
            )
            return_list.append(return_tuple)
    return return_list


def retrieve_course(course_name: str) -> dict:
    return_dict = {}

    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    request = urllib.request.urlopen(url)
    course = json.loads(request.read())
    weeks = 0
    students = 0
    hours = 0
    exercises = 0

    for item in course:
        weeks += 1
        if course[item]["students"] > students:
            students = course[item]["students"]
        hours += course[item]["hour_total"]
        exercises += course[item]["exercise_total"]

    return_dict["weeks"] = weeks
    return_dict["students"] = students
    return_dict["hours"] = hours
    return_dict["hours_average"] = math.floor(hours / students)
    return_dict["exercises"] = exercises
    return_dict["exercises_average"] = math.floor(exercises / students)

    return return_dict
