# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    temp = {}
    temp["name"] = name
    temp["director"] = director
    temp["year"] = year
    temp["runtime"] = runtime
    database.append(temp) 