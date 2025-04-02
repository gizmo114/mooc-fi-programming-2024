from datetime import datetime

day = int(input("What day were you born in: "))
month = int(input("what month were you born in: "))
year = int(input("What year were you born in: "))

birth_date = datetime(year, month, day)
millenium = datetime(1999, 12, 31)

if birth_date > millenium:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {(millenium - birth_date).days} days old on the eve of the new millennium.")

