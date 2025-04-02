# Copy here code of line function from previous exercise
def line(num, text):
    char = ""
    if text == "":
        char = "*"
    else:
        char = text[0]
    
    print(char * num)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = size
    while i > 0:
        line(size, "#")
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
