monkeys = []
operations = []
divisors = []
results_true = []
results_false = []
inspects = []

with open('input') as file:
    content = file.readlines()
    for i in range(0, len(content), 7):
        monkeys.append([int(num) for num in content[i + 1].split(':')[-1].split(',')])
        operations.append(content[i + 2].strip().split('=')[-1].split()[-2:])
        divisors.append(int(content[i + 3].split()[-1]))
        results_true.append(int(content[i + 4].split()[-1]))
        results_false.append(int(content[i + 5].split()[-1]))
        inspects.append(0)

monkeys = [[[item % div for div in divisors] for item in monkey] for monkey in monkeys]
for _ in range(10000):
    for i in range(len(monkeys)):
        inspects[i] += len(monkeys[i])
        for item in monkeys[i]:
            if operations[i][0] == '+':
                new_item = [(it + int(operations[i][1])) % div for it, div in zip(item, divisors)]
            else:
                if 'old' == operations[i][1]:
                    new_item = [(it * it) % div for it, div in zip(item, divisors)]
                else:
                    new_item = [(it * (int(operations[i][1]) % div)) % div for it, div in zip(item, divisors)]
            monkeys[results_true[i] if not new_item[i] else results_false[i]].append(new_item)
        monkeys[i] = list()

inspects.sort(reverse=True)
print(inspects[0] * inspects[1])
