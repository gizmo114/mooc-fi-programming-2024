# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str) -> dict:
    return_dict = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            line_data = line.split(';')
            if line_data[0] == "Longitude":
                continue
            return_dict[line_data[3]] = (float(line_data[0]),float(line_data[1]))
    return return_dict

def distance(stations: dict, station1: str, station2: str) -> float:
    long1, lat1 = stations[station1]
    long2, lat2 = stations[station2]

    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km

def greatest_distance(stations: dict) -> tuple:
    temp = []
    temp_dict = {}
    returnple = ()
    greatest = 0
    for key, value in stations.items():
        temp.append(key)
    #generate list of all the unique pairs in the list
    for i in range(0,len(temp)):
        for j in range(0,len(temp)):
            if temp[i] == temp[j]:
                continue
            else:
                temple = (temp[i], temp[j])
                if tuple(sorted(list(temple))) not in temp_dict:
                    temp_dict[temple] = True
    
    for key, value in temp_dict.items():
        if distance(stations, key[0], key[1]) > greatest:
            greatest = distance(stations, key[0], key[1])
            returnple = (key[0], key[1], greatest)
    return returnple

