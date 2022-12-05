import sys

file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()


def overlaps(a_1, a_2, b_1, b_2):
    return a_1 <= b_1 <= a_2 or b_2 >= a_1 >= b_1


count = 0

for line_str in lines:
    elf_1, elf_2 = line_str.strip().split(',')
    elf_1_start, elf_1_end = map(int, elf_1.split('-'))
    elf_2_start, elf_2_end = map(int, elf_2.split('-'))

    if overlaps(elf_1_start, elf_1_end, elf_2_start, elf_2_end):
        count += 1

print(count)
