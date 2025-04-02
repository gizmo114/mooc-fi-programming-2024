#Write your solution here
tmp = []
exam_points = []
exercise_points = []
points = []


def user_input():
    line = ""
    i = 0
    while True:
        line = input("Exam points and exercises completed: ")
        if line == "":
            break
        
        tmp = line.split()
        exam_points.append(int(tmp[i]))
        exercise_points.append(int(tmp[i+1]))
    print_statistics(exam_points, exercise_points)

def print_statistics(exam: list, exercise: list):
    distribution = [0, 0, 0, 0, 0, 0]
    summy = 0
    i = 0
    j = 0
    k = 0
    m = 5
    points_average = 1.0
    stars = ""

    while i < len(exam_points):
        summy = exam_points[i] + (exercise_points[i] // 10)
        points.append(summy)
        i += 1
    
    while j < len(points):
        if exam_points[j] < 10 or points[j] < 15:
            distribution[0] += 1
        elif points[j] >= 15 and points[j] < 18:
            distribution[1] += 1
        elif points[j] >= 18 and points[j] < 21:
            distribution[2] += 1
        elif points[j] >= 21 and points[j] < 24:
            distribution[3] += 1
        elif points[j] >= 24 and points[j] < 28:
            distribution[4] += 1
        else:
            distribution[5] += 1
        j += 1
    pass_perc = ((distribution[1] + distribution[2] + distribution[3] + distribution[4] + distribution[5]) / sum(distribution)) * 100
    points_average = sum(points) / len(points)

    print("Statistics: ")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_perc:.1f}")
    print(f"Grade distribution: ")
    while m >= 0:
        stars = "*" * distribution[m]
        print(f"{m}: {stars}")
        m -= 1

user_input()
       