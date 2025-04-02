# Write your solution here
def find_movies(database: list, search_term: str):
    temp = []
    for movie in database:
        if search_term in movie["name"].lower():
            temp.append(movie)
    return temp