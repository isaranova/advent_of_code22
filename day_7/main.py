system = {'root': 0}
with open('input') as file:
    curr_dir = '/'
    for line in file.readlines():
        if '$ cd' in line:
            folder = line.strip().split()[-1]
            if folder == '/':
                curr_dir = 'root'
            elif folder != '..':
                curr_dir = f'{curr_dir}/{folder}'
            else:
                curr_dir = '/'.join(curr_dir.split('/')[:-1])
        elif '$ ls' in line:
            pass
        else:  # ls output
            if 'dir' in line:
                folder = line.strip().split()[-1]
                system[f'{curr_dir}/{folder}'] = 0
            else:
                size, _ = line.strip().split()
                for i in range(len(curr_dir.split('/'))):
                    system['/'.join(curr_dir.split('/')[:i + 1])] += int(size)

print(sum([size for size in system.values() if size <= 100000]))
print(min([size for size in system.values() if size >= 30000000 - 70000000 + system['root']]))