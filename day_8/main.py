with open('input') as file:
    trees = [[int(num) for num in line.strip()] for line in file.readlines()]

visibility = [[4 for _ in range(len(trees))] for _ in range(len(trees))]
scenic = [[1 for _ in range(len(trees))] for _ in range(len(trees))]
for i in range(len(trees)):
    for j in range(len(trees)):
        me = trees[i][j]
        for z in range(j + 1, len(trees)):
            if trees[i][z] >= me:
                scenic[i][j] *= (z - j)
                visibility[i][j] -= 1
                break
        else:
            scenic[i][j] *= (z - j) if j != len(trees) - 1 else 0

        for z in range(j - 1, -1, -1):
            if trees[i][z] >= me:
                scenic[i][j] *= (j - z)
                visibility[i][j] -= 1
                break
        else:
            scenic[i][j] *= (j - z) if j != 0 else 0

        for z in range(i + 1, len(trees)):
            if trees[z][j] >= me:
                scenic[i][j] *= (z - i)
                visibility[i][j] -= 1
                break
        else:
            scenic[i][j] *= (z - i) if i != len(trees) - 1 else 0

        for z in range(i - 1, -1, -1):
            if trees[z][j] >= me:
                scenic[i][j] *= (i - z)
                visibility[i][j] -= 1
                break
        else:
            scenic[i][j] *= (i - z) if i != 0 else 0

print(sum([sum([1 for vv in v if vv]) for v in visibility]), max([max(s) for s in scenic]))
