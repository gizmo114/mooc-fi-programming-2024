# Write your solution here
def line(num, text):
    char = ""
    if text == "":
        char = "*"
    else:
        char = text[0]
    
    print(char * num)
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")