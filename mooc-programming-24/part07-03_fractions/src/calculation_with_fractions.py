# Write your solution here
from fractions import Fraction

def fractionate(num: int) -> list:
    i = 0
    response = []
    #print(Fraction(1, num))
    while i < num:
        response.append(Fraction(1, num))
        i += 1
    return response

#for i in fractionate(3):
 #   print(i)