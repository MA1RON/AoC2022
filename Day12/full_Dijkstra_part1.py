from treelib import Node, Tree
from copy import *
import numpy as np
import matplotlib.pyplot as plt


def find_possible_coo(chart,coo):
    global dim0,dim1
    possible_coo = []
    if coo[0] != 0: # not LEFT edge
        if ord(chart[coo[0]-1][coo[1]]) <= ord(chart[coo[0]][coo[1]])+1:
            possible_coo.append((coo[0]-1,coo[1]))
    if coo[0] != dim1-1: # not RIGHT edge
        if ord(chart[coo[0]+1][coo[1]]) <= ord(chart[coo[0]][coo[1]])+1:
            possible_coo.append((coo[0]+1,coo[1]))
    if coo[1] != 0: # not TOP edge
        if ord(chart[coo[0]][coo[1]-1]) <= ord(chart[coo[0]][coo[1]])+1:
            possible_coo.append((coo[0],coo[1]-1))
    if coo[1] != dim0-1: # not BOTTOM edge
        if ord(chart[coo[0]][coo[1]+1]) <= ord(chart[coo[0]][coo[1]])+1:
            possible_coo.append((coo[0],coo[1]+1))
    return possible_coo


def remove_possible_coo(tree,possible_coo):
    global last_node
    added_something = False
    
    initial_possible_coo = possible_coo[:] # possible coo will change, initial won't
    for coo in initial_possible_coo:
        if coo in all_coos:
            possible_coo.remove(coo)
        else:
            last_node += 1
            tree.create_node(coo,last_node,current_node)
            all_coos.append(coo)
            added_something = True
    return tree,added_something,possible_coo


def myshow(tree):
    board = np.zeros((dim1,dim0))
    
    # draw geo
    for row in range(dim1):
        for col in range(dim0):
            board[row,col] = ord(chart[row][col])-ord('a')
    
    # draw route
    par = int(current_node)
    while tree.parent(par).tag != start_coordinates:
        # print(tree[par].tag)
        board[tree[par].tag[0],tree[par].tag[1]] = -10
        par = tree.parent(par).identifier
    plt.pcolor(board)
    plt.show()


# read file
with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

# read variables
chart = [[]]
line_index = 0
for line in lines:
    c_index = 0
    for c in line:
        # find START
        if c == 'S':
            global start_coordinates
            start_coordinates = (line_index,c_index)
            chart[line_index].append('a')
            c_index += 1
        elif c == 'E':
            end_coordinates = (line_index,c_index)
            chart[line_index].append('z')
            c_index += 1
        
        # draw the chart
        elif c != '\n':
            chart[line_index].append(c)
            c_index += 1
        else:
            chart.append([])
            line_index += 1
dim0 = len(line)
dim1 = len(chart)
all_coos = [start_coordinates]

# find the best path
tree = Tree() # just one
last_node = 0
current_node = 0
tree.create_node(start_coordinates,current_node)
coo = list(start_coordinates)
end_flag = False
while not end_flag:
    # where can I go
    possible_coo = find_possible_coo(chart,tree[current_node].tag)
    
    # remove coordinates where I've already been (it's shorter)
    # and put all the suitable children on the tree
    tree,added_something,possible_coo = remove_possible_coo(tree,possible_coo)
    
    # tree.show()
    current_node += 1
    
    # if no more paths end
    if not current_node in tree:
        end_flag = 2 # negative ending
    # if I arrived end
    elif tree[current_node].tag == end_coordinates:
        end_flag = 1 # positive ending

if end_flag == 1:
    best_path = tree.depth()-1 # to fix
    print(f'The algothim found a solution.\nThe best path length is: {best_path}')
    myshow(tree)
if end_flag == 2:
    print(f'No solutions :(')