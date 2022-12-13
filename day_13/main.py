import json
from functools import cmp_to_key


def compare(l1, l2):
    if not l1 or not l2:
        return -1 if l1 == l2 else 1 if len(l1) < len(l2) else 0
    i = 0
    while(42):
        el1 = l1[i]
        el2 = l2[i]
        result = -1  # undecided
        if isinstance(el1, int) and isinstance(el2, int) and el1 != el2:
            result = 1 if el1 < el2 else 0
        elif isinstance(el1, list) and isinstance(el2, int):
            result = compare(el1, [el2])
        elif isinstance(el1, int) and isinstance(el2, list):
            result = compare([el1], el2)
        elif isinstance(el1, list) and isinstance(el2, list):
            result = compare(el1, el2)

        if result == -1:
            i += 1
            if i >= len(l2):
                return 0 if len(l1) != len(l2) else -1
            if i >= len(l1):
                return 1 if len(l1) != len(l2) else -1
        else:
            return result


def to_cmp(l1, l2):
    result = compare(l1, l2)
    if result == -1:
        return 0
    elif result == 0:
        return -1
    else:
        return result


results = []
sortie = [[[2]], [[6]]]
with open('input.txt') as file:
    content = file.readlines()
    sortie.extend([json.loads(c.strip()) for c in content if c.strip()])
    for i in range(0, len(content), 3):
        results.append(compare(json.loads(content[i].strip()), json.loads(content[i + 1].strip())))
    sortie = sorted(sortie, key=cmp_to_key(to_cmp), reverse=True)

print(sum([i + 1 for i in range(len(results)) if results[i]]))
print((sortie.index([[2]]) + 1) * (sortie.index([[6]]) + 1))