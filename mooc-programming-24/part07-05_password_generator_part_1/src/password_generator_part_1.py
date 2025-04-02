# Write your solution here
from random import choice

def generate_password(length: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = ""

    for i in range(0,length):
        password += choice(alphabet)
    return password

#print(generate_password(8))