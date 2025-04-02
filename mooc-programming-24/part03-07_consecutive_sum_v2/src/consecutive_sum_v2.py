# Write your solution here
limit = int(input("Limit: "))
i = 1
sum = 0
calculation = "1"

while sum < limit:
    sum += i
    if sum != 1:
        calculation += " + " + str(i)
    i += 1

print(f"The consecutive sum: {calculation} = {sum}")