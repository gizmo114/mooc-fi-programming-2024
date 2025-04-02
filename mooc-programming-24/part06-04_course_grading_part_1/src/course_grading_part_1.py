# write your solution here
if True:
    student_info_file = input("Student information: ")
    exercises_file = input("Exercises completed: ")
else:
    student_info_file = "students1.csv"
    exercises_file = "exercises1.csv"
students = {}
exercises = {}

with open(student_info_file) as new_file:
    for line in new_file:
        student_data = line.split(";")
        if student_data[0] == "id":
            continue
        name = student_data[1].strip() + " " + student_data[2].strip()
        students[student_data[0]] = name

with open(exercises_file) as new_file:
    for line in new_file:
        total_exercises = 0
        exercise_data = line.split(";")
        if exercise_data[0] == "id":
            continue
        for data in exercise_data[1:]:
            total_exercises += int(data)
        exercises[exercise_data[0]] = total_exercises

for key, value in students.items():
    print(f"{value} {exercises[key]}")