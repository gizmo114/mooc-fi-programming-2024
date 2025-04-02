# Write your solution here
def add_student(database: dict, name: str):
    database[name] = []
    return database

def print_student(database: dict, name: str):
    if name in database:
        print(f"{name}: ")
        if len(database[name]) > 0:
            average = 0
            print(f" {len(database[name])} completed courses:")
            for course, grade in database[name]:
                print(f"  {course} {grade}")
                average += grade
            print(f" average grade {average / len(database[name]):.1f}")
        else:
            print (" no completed courses")
    else:
        print(f"{name}: no such person in the database")

def add_course(database: dict, name: str, course: tuple):
    sorted_tuple_list = []
    temp = []
    new_tuple_list = []

    database[name].append(course)
    #we sort the list of tupples, if subject names are the same they sort by grade
    # and we add [::-1] to start from greatest thus eliminating same course with lower grade
    #In the end we  have a list subject, grade, ... with each subject being there only once
    # and highest possible grade
    sorted_tuple_list = sorted(database[name])[::-1]
    for subject, grade in sorted_tuple_list:
        if subject not in temp and grade > 0:
            temp.append(subject)
            temp.append(grade)
    
    #we now for pairs from sorted list (only even numbering) and add them to another list
    # which then goes to the student
    for i in range(len(temp) - 1):
        pair = temp[i], temp[i + 1]
        if pair not in new_tuple_list and i % 2 == 0:
            new_tuple_list.append(pair)
    
    database[name] = new_tuple_list  

def summary(database: dict): 
    most_courses = 0
    most_courses_name = ""
    average_list = []
    highest_average = 0
    highest_average_name = ""
    
    for key, value in database.items():
        if len(database[key]) > most_courses:
            most_courses = len(database[key])
            most_courses_name = key
    
    for key, value in database.items():
        student_name = key
        courses_count = len(database[key])
        grades_total = 0
        for entry in database[key]:
            grades_total += entry[1]
        average_list.append(key)
        average_list.append(grades_total / courses_count)

    for i in range(0, len(average_list)):
        if i % 2 != 0 and average_list[i] > highest_average:
            highest_average = average_list[i]
            highest_average_name = average_list[i - 1]


    print(f"students {len(database)}")
    print(f"most courses completed {most_courses} {most_courses_name}")
    print(f"best average grade {highest_average} {highest_average_name}")



if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
    