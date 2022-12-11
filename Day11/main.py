import math

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

# read file
monkey_num = -1
objects = []
operations = []
divisible_by = []
throw_to = []
for line in lines:
    if 'Monkey' in line:
        objects.append([])
        monkey_num += 1
    elif 'Starting items' in line:
        elements = line.split(' ')
        for element in elements[4:]:
            objects[monkey_num].append(int(element[:-1]))
    elif 'Operation' in line:
        elements = line.split(' ')
        operations.append((elements[5],elements[6],elements[7][:-1])) # (num1,operation,num2)
    elif 'Test' in line:
        elements = line.split(' ')
        divisible_by.append(int(elements[-1][:-1]))
    elif 'If true' in line:
        elements = line.split(' ')
        throw_if_true = int(elements[-1][:-1])
    elif 'If false' in line:
        elements = line.split(' ')
        throw_if_false = elements[-1]
        throw_if_false = int(throw_if_false.replace('\n',''))
        throw_to.append((throw_if_true,throw_if_false))

supermodulo = math.prod(divisible_by)
inspect = [ 0 for y in range( len(objects) ) ]
n_rounds = 10000
for round_index in range(n_rounds):
    for monkey in range(len(objects)):
        while objects[monkey] != []:
            inspect[monkey] += 1
            
            element = objects[monkey][0]
            # operation
            if operations[monkey][0] == 'old':
                num1 = int(element)
            else:
                num1 = int(operations[monkey][0])
            if operations[monkey][2] == 'old':
                num2 = int(element)
            else:
                num2 = int(operations[monkey][2])
            if operations[monkey][1] == '*': # *
                obj = num1 * num2
            else: # +
                obj = num1 + num2
                
            # redue the number
            # obj = obj // 3 # part 1
            obj = obj % supermodulo # part 2
            
            # throw away
            if obj % divisible_by[monkey] == 0:
                objects[throw_to[monkey][0]].append(obj)
            else:
                objects[throw_to[monkey][1]].append(obj)
            objects[monkey].pop(0)

print(objects)
print(inspect)

m1 = max(inspect)
inspect.remove(m1)
m2 = max(inspect)
print(m1*m2)