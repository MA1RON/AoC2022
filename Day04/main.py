import os
os.chdir('/Users/matteocanducci/Documents/Advent of Code 2022/Day04')
import numpy as np

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

# part 1
elf_useless = 0
elf_overlap = 0
for line in lines:
    line = line.replace('\n','')
    [str1,str2] = line.split(",")
    [ind_in_1,ind_fi_1] = str1.split("-")
    [ind_in_2,ind_fi_2] = str2.split("-")
    if (int(ind_in_1) >= int(ind_in_2) and int(ind_fi_1) <= int(ind_fi_2)) or \
        (int(ind_in_2) >= int(ind_in_1) and int(ind_fi_2) <= int(ind_fi_1)):
        elf_useless += 1
    if (int(ind_in_2) >= int(ind_in_1) and int(ind_in_2) <= int(ind_fi_1)) or \
        (int(ind_fi_2) >= int(ind_in_1) and int(ind_fi_2) <= int(ind_fi_1)) or \
        (int(ind_in_1) >= int(ind_in_2) and int(ind_in_1) <= int(ind_fi_2)) or \
        (int(ind_fi_1) >= int(ind_in_2) and int(ind_fi_1) <= int(ind_fi_2)):
        elf_overlap += 1
    # print(f'line "{line}": {elf_overlap}.')
print(elf_useless)
print(elf_overlap)