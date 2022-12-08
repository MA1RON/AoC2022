import os
os.chdir('/Users/matteocanducci/Documents/Advent of Code 2022/Day07')
from treelib import Node, Tree

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

tree = Tree()
tree.create_node('root','root')
dir_list = {'root': 0}
file_list = []

pwd = 'root' # I use 'root' instead of /
for line in lines[1:]:
    line = line.replace('\n','')
    # change directory
    if line[:4] == '$ cd':
        if line[5] == '/': # specific directory in the full tree
            pwd = 'root' + line[5:] # you would have to create all the new folders
        elif line[5:7] == '..': # previous directory
            pwdv = pwd.split('/')
            pwd_parent = pwd[:]
            pwd = '/'.join(pwdv[:-1])
        else: # specific directory in the folder
            pwdv = pwd.split('/')
            if not pwd in dir_list:
                dir_list[pwd] = 0
                tree.create_node(pwd,pwd, parent=pwd_parent)
            pwd += '/' + line[5:]
    # ignore ls
    elif line[:4] == '$ ls':
        pass
    # new dir
    elif line[:4] == 'dir ':
        pwdv = pwd.split('/')
        linev = line.split(' ')
        if not pwd+'/'+linev[-1] in dir_list:
            dir_list[pwd+'/'+linev[-1]] = 0
            tree.create_node(pwd+'/'+linev[-1],pwd+'/'+linev[-1], parent=pwd)
        else:
            pass # we're see a dir already saved
    # new file
    else:
        linev = line.split(' ')
        pwdv = pwd.split('/')
        if pwdv[-1] != 'root':
            name = pwd[:]
        else:
            name = pwdv[-1]
        if not pwd+'/'+linev[1] is file_list:
            file_list.append(pwd+'/'+linev[1])
            for pwdind in range(len(pwdv)):
                dir_list[name] += int(linev[0])
                name_v = name.split('/')
                if name_v[-1] != 'root':
                    if tree.parent(name).identifier != 'root':
                        name = pwd[:pwd.index(name_v[-1])-1]
                    else:
                        name = 'root'
        else:
            pass # we're see a document already saved
                    
# point 1
limit = 100000
result = 0
for dir in dir_list:
    if dir_list[dir] <= limit:
        result += dir_list[dir]
# tree.show(line_type="ascii-em")
print(result)

# point 2
total_space = 70000000
total_to_free_space = 30000000
empty_space = total_space-dir_list['root']
to_free_space = total_to_free_space - empty_space
dir_list = dir_list.values()
dir_list = sorted(dir_list,reverse=True)

jj = 0
for dir in dir_list:
    if dir <= to_free_space:
        print(dir_list[jj-1])
        break
    jj += 1