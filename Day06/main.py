import os
os.chdir('/Users/matteocanducci/Documents/Advent of Code 2022/Day06')
import numpy as np

def has_repetitions(s):
    flag = False
    ind = 0
    for c in s:
        s_ = [x for i,x in enumerate(s) if i!=ind]
        if c in s_:
            flag = True
        ind += 1
    return flag

with open('input_data.txt','r') as f:
    line = f.readlines()
f.close()
line = line[0]

ind = 3
flag_som = False
flag_sop = False
while ind < len(line) and not flag_som:
    if not has_repetitions(line[ind-3:ind+1]) and not flag_sop:
        print(f'First start-of-packet marker is {line[ind]} at position {ind+1}.')
        flag_sop = True
    if ind >= 13:
        if not has_repetitions(line[ind-13:ind+1]):
            print(f'First start-of-message marker is {line[ind]} at position {ind+1}.')
            flag_som = True
    ind += 1