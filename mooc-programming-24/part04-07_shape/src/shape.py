# Copy here code of line function from previous exercise and use it in your solution
def line(num, text):
    char = ""
    if text == "":
        char = "*"
    else:
        char = text[0]
    
    print(char * num)

def triangle(size, char):
    # You should call function line here with proper parameters
    i = 1

    while i <=size:
        line(i, char)
        i += 1

def rectangle(height, width, char):
    # You should call function line here with proper parameters
    i = height
    while i > 0:
        line(width, char)
        i -= 1
def shape(triangle_size, triangle_char, rectangle_height, rectangle_char):
    triangle(triangle_size, triangle_char)
    rectangle(rectangle_height, triangle_size, rectangle_char)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")