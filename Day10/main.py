def printCRT(sprite,register):
    if register in [sprite-1,sprite,sprite+1]:
        print('.',end='')
    else:
        print(' ',end='')
    if sprite == 39:
        print('')
        sprite = -1
    sprite += 1
    return sprite

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

sprite = 0
result = 0
global to_check
to_check = [20, 60, 100, 140, 180, 220]
cycle = 0
register = 1
for line in lines:
    line = line.replace('\n','')
    if line == 'noop':
        cycle += 1
        sprite = printCRT(sprite,register)
        if cycle in to_check:
            result += register*cycle
    else:
        _,additive = line.split(' ')
        cycle += 1
        sprite = printCRT(sprite,register)
        if cycle in to_check:
            result += register*cycle
            flag = True
        cycle += 1
        sprite = printCRT(sprite,register)
        if cycle in to_check:
            result += register*cycle
        
        register += int(additive)
print(result)