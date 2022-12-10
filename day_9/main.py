import math

move = {
    'L': [-1, 0], 'R': [1, 0], 'D': [0, -1], 'U': [0, 1], 'UL': [-1, 1], 'UR': [1, 1], 'DL': [-1, -1], 'DR': [1, -1]
}


def update_pos(pos, operation):
    pos[0] += move[operation][0]
    pos[1] += move[operation][1]


def switcherino(pos1, pos2):
    if math.dist(pos1, pos2) <= math.sqrt(2):
        return
    if pos1[0] == pos2[0] and pos1[1] > pos2[1]:  # on same y axis
        update_pos(pos2, 'U')
    elif pos1[0] == pos2[0] and pos1[1] < pos2[1]:
        update_pos(pos2, 'D')
    elif pos1[0] < pos2[0] and pos1[1] == pos2[1]:
        update_pos(pos2, 'L')
    elif pos1[0] > pos2[0] and pos1[1] == pos2[1]:
        update_pos(pos2, 'R')
    elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
        update_pos(pos2, 'UL')
    elif pos1[0] > pos2[0] and pos1[1] > pos2[1]:
        update_pos(pos2, 'UR')
    elif pos1[0] < pos2[0] and pos1[1] < pos2[1]:
        update_pos(pos2, 'DL')
    elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
        update_pos(pos2, 'DR')
    else:
        print('WTF')


h = [0, 0]
t = [[0, 0] for _ in range(9)]
visited = {(0, 0)}
visited2 = {(0, 0)}
with open('input') as file:
    for line in file.readlines():
        operation, repeats = line.strip().split()
        for _ in range(int(repeats)):
            update_pos(h, operation)
            follow = h
            for tail in t:
                switcherino(follow, tail)
                follow = tail
            visited.add((t[0][0], t[0][1]))
            visited2.add((t[-1][0], t[-1][1]))

print(len(visited), len(visited2))