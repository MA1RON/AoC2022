import os
os.chdir('/Users/matteocanducci/Documents/Advent of Code 2022/Day05')
import numpy as np

with open('input_data.txt','r') as f:
    lines_initial_state = f.readlines()
f.close()

with open('movements.txt','r') as f:
    lines_ordering = f.readlines()
f.close()

# save the crates
number_of_col = 9
crates = [[],[],[],[],[],[],[],[],[]]
for row in lines_initial_state:
    c = 0
    while c < len(row):
        if row[c] == '[' and row[c+2] == ']':
            col = int(c/4)
            crates[col].append(row[c+1])
        c += 4

# turn the columns upside down
for col in range(number_of_col):
    crates[col].reverse()

# move the crates
for line in lines_ordering:
    words = line.split(' ')
    words[5] = words[5][0]
    tomove = crates[int(words[3])-1][-(int(words[1])):]
    # tomove.reverse() # commented for part 2, uncommented for part 1
    for crate in tomove:
        crates[int(words[5])-1].append(crate)
    for crate in range(len(tomove)):
        crates[int(words[3])-1].pop(len(crates[int(words[3])-1])-1)
    tomove = []


# take the last ones
final_string = ''
for col in range(number_of_col):
    print(crates[col])
    final_string += crates[col][-1]
print(final_string)
