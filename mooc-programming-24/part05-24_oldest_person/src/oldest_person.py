# Write your solution here
def oldest_person(people: list):
    oldest = people[0][1]
    name = people[0][0]
    for human in people:
        if human[1] < oldest:
            oldest = human[1]
            name = human[0]
    return name