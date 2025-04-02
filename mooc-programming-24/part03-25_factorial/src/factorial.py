# Write your solution here
i = 1
result = 1

while True:
    num = int(input("Please type in a number: "))
    result = 1
    i = 1
    if num <= 0:
        break
    else:
        while i <= num:
            result *= i
            i += 1
    print(f"The factorial of the number {num} is {result}")

print("Thanks and bye!")
