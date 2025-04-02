class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list) -> list:
    return list(filter(lambda ca: ca.grade >= 1, attempts))

def attempts_with_grade(attempts: list, grade: int) -> list:
    return list(filter(lambda ca: ca.grade == grade, attempts))

def passed_students(attempts: list, course: str) -> list:
    return sorted(list(map(lambda ca : ca.student_name, list(filter(lambda ca: ca.course_name == course and ca.grade > 0, attempts)))))