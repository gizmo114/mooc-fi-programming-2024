# Write your solution here
caf = int(input("How many times a week do you eat at the student cafeteria?" ))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? \n"))
weekly = caf*price+groceries
print("Average food expenditure:")
print(f"Daily: {weekly/7} euros")
print(f"Weekly: {weekly} euros")