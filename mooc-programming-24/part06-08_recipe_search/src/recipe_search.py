# Write your solution here
def read_file(file: str) -> list:
    recipes = []
    with open(file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            recipes.append(line)
    return recipes
   
def create_recipes(file: str) -> list:
    return_list = []
    recipes = read_file(file)
    total_recipes = recipes.count("") + 1
    start = 0
    for i in range(total_recipes):
        temp = {}
        temp['name'] = recipes[start]
        temp['prep_time'] = recipes[start+1]
        try:
            end = recipes.index('', start)
        except:
            end = len(recipes)
        temp['ingredients'] = recipes[start+2:end]
        start = end + 1
        return_list.append(temp)
    return return_list

def search_by_name(file: str, word: str) -> list:
    recipes = create_recipes(file)
    found = []
    for i in range(len(recipes)):
        if word.lower() in recipes[i]['name'].lower():
            found.append(recipes[i]['name']) 
    return found

def search_by_time(file: str, prep_time: int) -> list:
    recipes = create_recipes(file)
    found = []
    for i in range(len(recipes)):
        if int(recipes[i]['prep_time']) <= prep_time:
            return_string = recipes[i]['name'] + ", preparation time " + recipes[i]['prep_time'] + " min"
            found.append(return_string)
    return found

def search_by_ingredient(file: str, ingredient: str) -> list:
    recipes = create_recipes(file)
    found = []
    for i in range(len(recipes)):
        for entry in recipes[i]['ingredients']:
            if ingredient.lower() in entry.lower():
                return_string = recipes[i]['name'] + ", preparation time " + recipes[i]['prep_time'] + " min"
                found.append(return_string)
    return found








            