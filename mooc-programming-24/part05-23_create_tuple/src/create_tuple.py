# Write your solution here
def smallest(x: int, y: int, z:int):
    if (x < y) and (x < z):
        return x
    elif (y < z):
        return y
    else:
        return z

def greatest(x: int, y: int, z:int):
    if (x > y) and (x > z):
        return x
    elif (y > z):
        return y
    else:
        return z

def create_tuple(x: int, y: int, z: int):
    tuplee = (smallest(x, y, z), greatest(x, y, z), x + y + z)
    return tuplee