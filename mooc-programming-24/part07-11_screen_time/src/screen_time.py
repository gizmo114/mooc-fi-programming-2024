from datetime import datetime, timedelta

filename = input("Filename: ")
starting_date_string = input("Starting date: ")
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile): ")

starting_date = datetime.strptime(starting_date_string, "%d.%m.%Y")
output_starting_date = datetime.strftime(starting_date, "%d.%m.%Y")

screen_time = {}
for i in range(days):
    end_date = datetime.strftime(starting_date, "%d.%m.%Y")
    screen_time[end_date] = input(f"Screen time {end_date}: ").split(" ")
    starting_date += timedelta(days=1)

total = 0
for key, value in screen_time.items():
    for item in value:
        total += int(item)
average = total / days

with open(filename, "w") as file:
    file.write(f"Time period: {output_starting_date}-{end_date}\n")
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {average}\n")
    for key, value in screen_time.items():
        file.write(f"{key}: {value[0]}/{value[1]}/{value[2]}\n")
file.close()
