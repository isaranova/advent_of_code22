elves = [0]
with open('input') as file:
    for line in file.readlines():
        if not line.strip():
            elves.append(0)
            continue
        elves[-1] += int(line.strip())
print(max(elves))  # part 1
print(sum(sorted(elves, reverse=True)[:3]))  # part 2
