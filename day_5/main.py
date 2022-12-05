stacks = {}
stacks2 = {}
with open('input') as file:
    for line in file.readlines():
        if 'move' in line:
            cnt, src, dst = [int(n) for n in line.strip().split()[1::2]]
            stacks[dst] = list(reversed(stacks[src][:cnt])) + stacks[dst]
            stacks[src] = stacks[src][cnt:]
            stacks2[dst] = stacks2[src][:cnt] + stacks2[dst]
            stacks2[src] = stacks2[src][cnt:]
        elif '[' in line:
            l = list(line)[1::4]
            for i in range(len(l)):
                if l[i] == ' ':
                    continue
                if i + 1 not in stacks:
                    stacks[i + 1] = [l[i]]
                    stacks2[i + 1] = [l[i]]
                else:
                    stacks[i + 1].append(l[i])
                    stacks2[i + 1].append(l[i])

print(''.join([stacks[i][0] for i in range(1, len(stacks) + 1)]))
print(''.join([stacks2[i][0] for i in range(1, len(stacks) + 1)]))
