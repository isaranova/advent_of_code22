sum = 0
sum2 = 0
with open('input.txt') as file:
    for line in file.readlines():
        fe, se = [set(range(int(r.split('-')[0]), int(r.split('-')[1]) + 1)) for r in line.strip().split(',')]
        if fe.issubset(se) or se.issubset(fe):
            sum += 1
        if fe.intersection(se):
            sum2 += 1
print(sum)
print(sum2)