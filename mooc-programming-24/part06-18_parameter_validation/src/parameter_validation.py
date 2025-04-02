# Write your solution here
def new_person(name: str, age: int) -> tuple:
    if name == '' or len(name.split(' ')) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError('Something went wrong!')
    else:
        return(name,age)