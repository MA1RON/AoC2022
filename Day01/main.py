with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

elf_calories = [0]
elf_index = 0
for line in lines:
    if line == '\n': # spazio vuoto
        elf_index += 1
        elf_calories.append(0)
    else:
        elf_calories[elf_index] += int(line)

# part 1
elf_calories.sort()
elf_fat = elf_calories[-1]
print(elf_fat)
# part 2
elf_fat3 = elf_calories[-3] + elf_calories[-2] + elf_calories[-1]
print(elf_fat3)
    
