# Copy here code of line function from previous exercise
def line(num, text):
    char = ""
    if text == "":
        char = "*"
    else:
        char = text[0]
    
    print(char * num)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = height
    while i > 0:
        line(10, "#")
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
