def newrope(rope,knot):
    if (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==0): # U
        rope[knot][1] += 1
    elif (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==1) or \
            (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==2) or \
            (rope[knot-1][1]-rope[knot][1]==1 and rope[knot-1][0]-rope[knot][0]==2): # U R
        rope[knot][0] += 1
        rope[knot][1] += 1
    elif (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==-1) or \
            (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==-2) or \
            (rope[knot-1][1]-rope[knot][1]==1 and rope[knot-1][0]-rope[knot][0]==-2): # U L
        rope[knot][0] -= 1
        rope[knot][1] += 1
    if (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==0): # D
        rope[knot][1] -= 1
    elif (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==1) or \
            (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==2) or \
            (rope[knot-1][1]-rope[knot][1]==-1 and rope[knot-1][0]-rope[knot][0]==2): # D R
        rope[knot][0] += 1
        rope[knot][1] -= 1
    elif (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==-1) or \
            (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==-2) or \
            (rope[knot-1][1]-rope[knot][1]==-1 and rope[knot-1][0]-rope[knot][0]==-2): # D L
        rope[knot][0] -= 1
        rope[knot][1] -= 1
    if (rope[knot-1][1]-rope[knot][1]==0 and rope[knot-1][0]-rope[knot][0]==2): # R
        rope[knot][0] += 1
    elif (rope[knot-1][1]-rope[knot][1]==1 and rope[knot-1][0]-rope[knot][0]==2) or \
            (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==2) or \
            (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==1): # U R
        rope[knot][0] += 1
        rope[knot][1] += 1
    elif (rope[knot-1][1]-rope[knot][1]==-1 and rope[knot-1][0]-rope[knot][0]==2) or \
            (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==2) or \
            (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==1): # D R
        rope[knot][0] += 1
        rope[knot][1] -= 1
    if (rope[knot-1][1]-rope[knot][1]==0 and rope[knot-1][0]-rope[knot][0]==-2): # L
        rope[knot][0] -= 1
    elif (rope[knot-1][1]-rope[knot][1]==1 and rope[knot-1][0]-rope[knot][0]==-2) or \
            (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==-2) or \
            (rope[knot-1][1]-rope[knot][1]==2 and rope[knot-1][0]-rope[knot][0]==-1): # U L
        rope[knot][0] -= 1
        rope[knot][1] += 1
    elif (rope[knot-1][1]-rope[knot][1]==-1 and rope[knot-1][0]-rope[knot][0]==-2) or \
            (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==-2) or \
            (rope[knot-1][1]-rope[knot][1]==-2 and rope[knot-1][0]-rope[knot][0]==-1): # D L
        rope[knot][0] -= 1
        rope[knot][1] -= 1
    return rope

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

rope_len = 10
rope = []
_ = [rope.append([0,0]) for j in range(rope_len)]
visited = []
for line in lines:
    [direction,distance] = line.split(' ')
    distance.replace('\n','')
    # usa 5 casi , differenza orizzontale, differenza verticale, diagonale, e cavallo sono 2
    for step in range(int(distance)):
        if direction == 'U':
            rope[0][1] += 1
            for knot in range(1,rope_len):
                rope = newrope(rope,knot)
        if direction == 'D':
            rope[0][1] -= 1
            for knot in range(1,rope_len):
                rope = newrope(rope,knot)
        if direction == 'R':
            rope[0][0] += 1
            for knot in range(1,rope_len):
                rope = newrope(rope,knot)
        if direction == 'L':
            rope[0][0] -= 1
            for knot in range(1,rope_len):
                rope = newrope(rope,knot)
        if not rope[rope_len-1] in visited:
            visited.append(rope[rope_len-1][:])

print(len(visited))