from treelib import Node, Tree
from copy import *


def find_possible_coo(chart,coo):
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


def add_possible_coo(tree,possible_coo,coo):
    added_something = False
    
    initial_possible_coo = possible_coo[:]
    for check_coo in initial_possible_coo:
        if coo == list(start_coordinates):
            tree.create_node(check_coo,check_coo,parent=tuple(coo))
            added_something = True
        else:
            # to be checked when they actually have sons
            it_started = False
            is_repetitive = False
            if check_coo != start_coordinates:
                parent_coo = coo[:]
                while parent_coo != start_coordinates and not is_repetitive:
                    it_started = True
                    
                    childs = []
                    for child in tree.children(tree.parent(parent_coo).identifier):
                        childs.append(child.identifier)
                    
                    if check_coo in childs:
                        is_repetitive = True
                    else:
                        parent_coo = tree.parent(parent_coo).identifier
            if not is_repetitive and it_started:
                tree.create_node(check_coo,check_coo,parent=coo)
                added_something = True
            else:
                possible_coo.remove(check_coo)
    return tree,added_something,possible_coo


def cancel_coo(tree,coo):
    end_flag = False
    parent_coo = coo
    flag = False
    while not flag:
        old_coo = parent_coo[:]
        parent_coo = tree.parent(parent_coo).identifier
        tree.remove_node(old_coo)
        
        if tree.depth() != 0:
            if len(tree.children(tree.parent(parent_coo).identifier)) > 1:
                coo = tree.children(tree.parent(parent_coo).identifier)[1]
                coo = coo.identifier
                tree.remove_node(parent_coo)
                flag = True
        else: # no possible solutions
            flag = True
            end_flag = True
    
    return tree,coo,end_flag


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
global dim0
global dim1
dim0 = len(line)
dim1 = len(chart)

# find the best path
trees = []
trees_length = []
tree = Tree()
tree.create_node(start_coordinates,start_coordinates)
coo = list(start_coordinates)
end_flag = False
while not end_flag:
    # where can I go
    possible_coo = find_possible_coo(chart,coo)
    
    # add in the tree checking if I'm going back to the same square
    last_tree = copy(tree)
    tree,added_something,possible_coo = add_possible_coo(tree,possible_coo,coo)
    
    if not added_something:
        tree,coo,end_flag = cancel_coo(tree,coo) # cancel until it has a brother
    else:
        coo = possible_coo[0]
    
    # am I arrived?
    if coo == end_coordinates:
        # tree.show()
        trees.append(tree)
        trees_length.append(tree.depth()+1)
        
        if len(trees) % 10 == 0:
            print('I did 10.')

print(min(trees_length))