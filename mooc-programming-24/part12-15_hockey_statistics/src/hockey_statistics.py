# I know this code looks bad a lot of repetition, printing could've been one function etc. I was tired, really wanted to finish this
import json

# open the file, read the data via json reader and return them as a list of directories
def file_handler(filename: str) -> list:
    with open(filename) as file:
        file_data = file.read()
    data = json.loads(file_data)
    return data

# prints the menu
def help():
    print("commands:")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")

# search for player by name, return it as a string
def search_and_list(players: list):
    name = input("name: ")
    for player in players:
        if player["name"] == name:
            print(f"{player["name"]:<21}{player["team"]:>3}{player["goals"]:>4} + {player["assists"]:>2} = {(player["goals"] + player["assists"]):>3}")

# add team from each player into a set to remove duplicates
def list_teams(players: list):
    teams = set()
    for player in players:
        teams.add(player["team"])
    for team in sorted(list(teams)):
        print(team)

# same but countries
def list_countries(players: list):
    countries = set()
    for player in players:
        countries.add(player["nationality"])
    for cnt in sorted(list(countries)):
        print(cnt)

# sort all players by points and just print ones with matching team
def players_by_team(players: list):
    team = input("team: ")
    for player in sorted(players, key=lambda dir: dir["goals"] + dir["assists"], reverse=True):
        if player["team"] == team:
            print(f"{player["name"]:<21}{player["team"]:>3}{player["goals"]:>4} + {player["assists"]:>2} = {(player["goals"] + player["assists"]):>3}")

# same but country
def players_by_country(players: list):
    country = input("country: ")
    for player in sorted(players, key=lambda dir: dir["goals"] + dir["assists"], reverse=True):
        if player["nationality"] == country:
            print(f"{player["name"]:<21}{player["team"]:>3}{player["goals"]:>4} + {player["assists"]:>2} = {(player["goals"] + player["assists"]):>3}")

# sort by tuple, return sliced list
def most_points(players: list):
    num = int(input("how many: "))
    all_players_sorted = sorted(players, key=lambda dir: (dir["goals"] + dir["assists"], dir["goals"]), reverse=True)
    for player in all_players_sorted[:num]:
        print(f"{player["name"]:<21}{player["team"]:>3}{player["goals"]:>4} + {player["assists"]:>2} = {(player["goals"] + player["assists"]):>3}")
        
# same but different sort
def most_goals(players):
    num = int(input("how many: "))
    all_players_sorted = sorted(players, key=lambda dir: (dir["goals"], -dir["games"]), reverse=True)
    for player in all_players_sorted[:num]:
        print(f"{player["name"]:<21}{player["team"]:>3}{player["goals"]:>4} + {player["assists"]:>2} = {(player["goals"] + player["assists"]):>3}")

def execute():
    filename = input("file name: ")
    players = file_handler(filename)
    print(f"read the data of {len(players)} players")
    print("")
    help()
    while True:
        print("")
        command = input("command: ")
        if command == "0":
            break
        elif command == "1":
            search_and_list(players)
        elif command == "2":
            list_teams(players)
        elif command == "3":
            list_countries(players)
        elif command == "4":
            players_by_team(players)
        elif command == "5":
            players_by_country(players)
        elif command == "6":
            most_points(players)
        elif command == "7":
            most_goals(players)
        else:
            help()

execute()