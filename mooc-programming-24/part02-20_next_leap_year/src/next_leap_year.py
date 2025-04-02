# Write your solution here
iterations = 0
year = int(input("Year: "))
yearr = year

while True:
    if (yearr % 4 == 0 and yearr % 100 != 0 or yearr % 400 == 0) and iterations != 0:
        break
    else:
        yearr += 1
        iterations += 1
print(f"The next leap year after {year} is {yearr}")

