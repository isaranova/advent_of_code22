with open('input') as file:
    code = file.readline()
    for same in [4, 14]:
        i = same - 1
        while(42):
            uniq = len(set([code[i - j] for j in range(same)]))
            i += same - uniq
            if uniq == same:
                print(i + 1)
                break
