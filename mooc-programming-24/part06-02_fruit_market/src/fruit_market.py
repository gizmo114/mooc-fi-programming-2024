# write your solution here
def read_fruits() -> dict:
    with open("fruits.csv") as new_file:
        fruit_market = {}
        for line in new_file:
            line = line.replace("\n", "")
            items = line.split(";")
            #print(items)
            fruit_market[items[0]] = float(items[1])
    return fruit_market

#read_fruits()