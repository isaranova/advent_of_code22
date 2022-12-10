when = [20, 60, 100, 140, 180, 220]
with open('input') as file:
    content = file.readlines()
    signals = ([0] if 'addx' in content[1] else []) + [num for x in
               [[0] if 'noop' in line else [0, int(line.split()[1])] for line in content]
               for num in x]

print(sum([(sum(signals[:w]) + 1) * w for w in when]))
print(''.join([
    ('#' if i % 40 in range(sum(signals[:i + 1]), sum(signals[:i + 1]) + 3) else '.') +
    ('\n' if i % 40 == 39 else '')
    for i in range(len(signals))
])[:-1])