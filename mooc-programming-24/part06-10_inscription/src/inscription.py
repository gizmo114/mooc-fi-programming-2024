# Write your solution here
name = input('Name: ')
file = input('File: ')

with open(file, 'w') as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
