sum = 0
with open('input') as file:
    for line in file.readlines():
        line = line.strip()
        same = set.intersection(set(line[:(len(line) // 2)]), set(line[(len(line) // 2):])).pop()
        sum += ord(same) - (96 if same > 'Z' else 38)
print(sum)

sum = 0
with open('input') as file:
    content = file.readlines()
    for i in range(0, len(content), 3):
        lines = [set(content[i + j].strip()) for j in range(3)]
        same = set.intersection(*lines).pop()
        sum += ord(same) - (96 if same > 'Z' else 38)
print(sum)