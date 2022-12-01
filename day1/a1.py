import sys

file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()

    max_cals = 0

    elf_cals = 0
    for l in lines:
        line = l.strip()
        if len(line) == 0:
            max_cals = max(max_cals, elf_cals)
            elf_cals = 0
        else:
            num = int(line)
            elf_cals += num

    print(max_cals)

