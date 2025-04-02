# Write your solution here
grade = int(input("Please provide points: "))

if grade >= 0 and grade < 50:
    print("Grade: fail")
elif grade >= 50 and grade < 60:
    print("Grade: 1")
elif grade >= 60 and grade < 70:
    print("Grade: 2")
elif grade >= 70 and grade < 80:
    print("Grade: 3")
elif grade >= 80 and grade < 90:
    print("Grade: 4")
elif grade >= 90 and grade <= 100:
    print("Grade: 5")
else:
    print("impossible!")