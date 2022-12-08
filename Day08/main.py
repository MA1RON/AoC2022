import os
os.chdir('/Users/matteocanducci/Documents/Advent of Code 2022/Day08')
import numpy as np

def is_visible(jline,jdigit,trees):
    height = trees[jline,jdigit]
    # check if it's on border
    if jline == 0 or jline == map_size or jdigit == 0 or jdigit == map_size:
        return True
    # check on its left
    if (trees[jline,:jdigit] < height).all():
        return True
    # check on its right
    if (trees[jline,jdigit+1:] < height).all():
        return True
    # check above
    if (trees[:jline,jdigit] < height).all():
        return True
    # check below
    if (trees[jline+1:,jdigit] < height).all():
        return True
    return False
        

def find_score(jline,jdigit,trees):
    height = trees[jline,jdigit]
    score = 1
    # on the bored scenic view = 0
    if jline == 0 or jline == map_size or jdigit == 0 or jdigit == map_size:
        return 0
    # check on its left
    temp = 0
    for tree in np.flip(trees[jline,:jdigit]):
        temp += 1
        if tree >= height:
            break
    score *= temp
    # check on its right
    temp = 0
    for tree in trees[jline,jdigit+1:]:
        temp += 1
        if tree >= height:
            break
    score *= temp
    # check above
    temp = 0
    for tree in np.flip(trees[:jline,jdigit]):
        temp += 1
        if tree >= height:
            break
    score *= temp
    # check below
    temp = 0
    for tree in trees[jline+1:,jdigit]:
        temp += 1
        if tree >= height:
            break
    score *= temp
    return score


with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

global map_size
map_size = len(lines)
trees = np.zeros((map_size,map_size))
number_of_trees_visible = 0
for jline in range(map_size):
    for jdigit in range(map_size):
        trees[jline,jdigit] = lines[jline][jdigit]

score = 0
for jline in range(map_size):
    for jdigit in range(map_size):
        if is_visible(jline,jdigit,trees):
            number_of_trees_visible += 1
        temp_score = find_score(jline,jdigit,trees)
        if temp_score > score:
            score = temp_score
print(number_of_trees_visible)
print(score)