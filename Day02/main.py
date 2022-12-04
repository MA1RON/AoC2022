import os
os.chdir('/Users/matteocanducci/Documents/Advent of Code 2022/Day02')
import numpy as np

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

# part 1
ad_move = []
my_move = []
points_tot = 0
for line in lines:
    [ad_move,my_move] = line.split()
    # lose
    if (ad_move == 'B' and my_move == 'X') or (ad_move == 'C' and my_move == 'Y') or (ad_move == 'A' and my_move == 'Z'):
        points_outcome = 0
    # tie
    elif (ad_move == 'A' and my_move == 'X') or (ad_move == 'B' and my_move == 'Y') or (ad_move == 'C' and my_move == 'Z'):
        points_outcome = 3
    # win
    elif (ad_move == 'C' and my_move == 'X') or (ad_move == 'A' and my_move == 'Y') or (ad_move == 'B' and my_move == 'Z'):
        points_outcome = 6
    if my_move == 'X':
        points_my_move = 1
    elif my_move == 'Y':
        points_my_move = 2
    elif my_move == 'Z':
        points_my_move = 3
    points_tot += points_outcome + points_my_move

print(points_tot)

# part 2
ad_move = []
my_move = []
points_tot = 0
for line in lines:
    [ad_move,my_move] = line.split()
    # lose
    if my_move == 'X':
        points_outcome = 0
        if ad_move == 'A': # I play C
            points_my_move = 3
        elif ad_move == 'B': # I play A
            points_my_move = 1
        elif ad_move == 'C': # I play B
            points_my_move = 2
    # tie
    elif my_move == 'Y':
        points_outcome = 3
        if ad_move == 'A': # I play A
            points_my_move = 1
        elif ad_move == 'B': # I play B
            points_my_move = 2
        elif ad_move == 'C': # I play C
            points_my_move = 3
    # win
    elif my_move == 'Z':
        points_outcome = 6
        if ad_move == 'A': # I play B
            points_my_move = 2
        elif ad_move == 'B': # I play C
            points_my_move = 3
        elif ad_move == 'C': # I play A
            points_my_move = 1
    points_tot += points_outcome + points_my_move

print(points_tot)