# Write your solution here
n = int(input("Layers: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lines = []
line = []

# how this works for layers = 3 as an example
# CCCCC
# start=1 finish=4 k=1(n-2)
# CBBBC
# start=2 finish=3 k=0
# CBABC
# now we got half of list done and just copy from second to last till first
# CBBBC
# CCCCC
# convert to strings and print

i = 0 # counter
temp_list = []
k = n-2 # second letter to use
start = 1 # first index wher letter is applied
finish = 2*n - 2 # second to last letter where the letter is applied

#initialize first line with all the same characters and add it to the list of lines
while  i <= finish:
   line.append(alphabet[k+1])
   i += 1
lines.append(line)

#cycle through alphabet and move start/finish to overwrite last line and append it
#at the end of this we should have more than half the list done
while k >= 0:
    new_line = lines[-1].copy()
    for i in range(start, finish):
        new_line[i] = alphabet[k]
    lines.append(new_line)
    k -= 1
    start += 1
    finish -= 1

temp_list = lines.copy() # create copy of what we got
temp_list.pop() # pop removes last item by default, so we get rid of duplicate line
temp_list.reverse() # reverse the list
lines.extend(temp_list) #join it to the original list

# print the lines
for word in lines:
    print(''.join(word))


#print(lines)
#print(temp_list)