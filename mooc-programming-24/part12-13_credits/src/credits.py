from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(courses: list):
    return reduce(lambda sum, item: sum + item.credits, courses, 0)

def sum_of_passed_credits(courses: list):
    return reduce(lambda sum, item: sum + item.credits, list(filter(lambda ca: ca.grade > 0, courses)), 0)

def average(courses: list):
    return reduce(lambda sum, item: sum + item.grade, list(filter(lambda ca: ca.grade > 0, courses)), 0) / len(list(filter(lambda ca: ca.grade > 0, courses)))