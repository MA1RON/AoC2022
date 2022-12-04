import numpy as np

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

# part 1
points = 0
for line in lines:
    line = line[:-1]
    str1 = line[:int(len(line)/2)]
    str2 = line[int(len(line)/2):]
    common_char = list(set(str1)&set(str2))
    if ord(common_char[0]) >= ord('a'):
        points += ord(common_char[0]) - ord('a') + 1
    else:
        points += ord(common_char[0]) - ord('A') + 27
    # print(f'line "{line}": {common_char[0]}, {points} points.')
print(points)

# part 2
points = 0
line_index = 1
for line in lines:
    line = line[:-1]
    if np.mod(line_index,3) == 1:
        str1 = str(line)
    elif np.mod(line_index,3) == 2:
        str2 = str(line)
    elif np.mod(line_index,3) == 0:
        str3 = str(line)
        common_char = list(set(str1)&set(str2)&set(str3))
        if ord(common_char[0]) >= ord('a'):
            points += ord(common_char[0]) - ord('a') + 1
        else:
            points += ord(common_char[0]) - ord('A') + 27
        # print(f'line "{line}": {common_char[0]}, {points} points.')
    line_index += 1
print(points)
