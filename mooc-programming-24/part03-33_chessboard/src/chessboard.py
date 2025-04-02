# Write your solution here
def chessboard(size):
    i = 1
    j = 1
    k = 0
    l = 1
    string = ""
    inverse = ""
    
    while j <= size:
        string += str(i)
        if i == 1:
            i -= 1
        else:
            i += 1
        j += 1

    while k <= len(string) - 1:
        if string[k] == "1":
            inverse += "0"
        else:
            inverse += "1"
        k += 1
    
    while l <= size:
        if l % 2 != 0:
            print(string)
        else:
            print(inverse)
        l += 1
# Testing the function
if __name__ == "__main__":
    chessboard(4)
