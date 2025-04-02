# Write your solution here
iterations = 0
sum = 0
negative = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))

    if num == 0:
        break

    if num < 0:
        negative += 1

    iterations += 1
    sum += num

print(f"Numbers typed in {iterations}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum/iterations}")
print(f"Positive numbers {iterations-negative}")
print(f"Negative numbers {negative}")