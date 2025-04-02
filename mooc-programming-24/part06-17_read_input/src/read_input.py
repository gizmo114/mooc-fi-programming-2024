# Write your solution here
def read_input(message: str, x: int, y: int) -> int:
    while True:
        try:
            input_string = int(input(message))
            if input_string in range(x, y+1):
                return input_string
        except ValueError:
            pass
        print(f'You must type in an integer between {x} and {y}')

#read_input('Please type in a number: ',5,10)
