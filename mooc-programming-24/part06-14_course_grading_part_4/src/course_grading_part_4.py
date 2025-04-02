def do_stuff_to_course(course_file: str) -> str:
    return_string = ''
    temp_list = []
    with open(course_file) as file:
        for line in file:
            temp = line.split(': ')
            if temp[0] == 'name':
                temp_list.append(temp[1].strip())
            else:
                temp_list.append(temp[1])
    return_string = f'{temp_list[0]}, {temp_list[1]} credits'
    return return_string

def underlining(text: str) -> str:
    i = 0
    return_string = ''
    while i <= len(text) - 1:
        return_string += '='
        i += 1
    return return_string

def save_results_to_a_file():
    open('results.txt', 'w').close()
    with open('results.txt', 'a') as file:
        file.write(f'{do_stuff_to_course(course_file)}\n')
        file.write(f'{underlining(do_stuff_to_course(course_file))}\n')
        file.write('name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n')
    for key, value in students.items():
        with open('results.txt', 'a') as file:
            file.write(f'{students[key]:30}{exercises[key]:<10}{int(((((exercises[key]/40)*100)//10))):<10}{exams[key]:<10}{int(pointz[key]):<10}{grades[key]:<10}\n')
            file.close()

def save_to_csv():
    line = ''
    open('results.csv', 'w').close()
    for key, value in grades.items():
        with open('results.csv', 'a') as file:
            line = key + ';' + students[key] + ';' + str(value) + '\n'
            file.write(line)
            file.close()    

if True:
    student_info_file = input("Student information: ")
    exercises_file = input("Exercises completed: ")
    exam_file = input("Exam points: ")
    course_file = input("Course information: ")
else:
    student_info_file = "students2.csv"
    exercises_file = "exercises2.csv"
    exam_file = "exam_points2.csv"
    course_file = "course2.txt"
students = {}
exercises = {}
exams = {}
pointz = {}
grades = {}

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

with open(exam_file) as new_file:
    for line in new_file:
        total_exam = 0
        exam_data = line.split(";")
        if exam_data[0] == "id":
            continue
        for data in exam_data[1:]:
            total_exam += int(data)
        exams[exam_data[0]] = total_exam
       
#for key, value in students.items():
#    print(f"{value} {exercises[key]}")

for key, value in exams.items():
    points = (((exercises[key] / 40) * 100) // 10) + exams[key]
    pointz[key] = points
    if points < 15:
#       print(f"{students[key]} 0")
        grades[key] = 0
    elif points >= 15 and points < 18:
#       print(f"{students[key]} 1")
        grades[key] = 1
    elif points >= 18 and points < 21:
#        print(f"{students[key]} 2")
        grades[key] = 2
    elif points >= 21 and points < 24:
#       print(f"{students[key]} 3") 
        grades[key] = 3
    elif points >= 24 and points < 28:
#        print(f"{students[key]} 4") 
        grades[key] = 4 
    else:
#        print(f"{students[key]} 5")
        grades[key] = 5

save_results_to_a_file()
save_to_csv()