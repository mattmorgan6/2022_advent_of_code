import sys

file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()


def check_if_inside(a_1, a_2, b_1, b_2):
    return a_1 <= b_1 and a_2 >= b_2


count = 0

for line_str in lines:
    elf_1, elf_2 = line_str.strip().split(',')
    elf_1_start, elf_1_end = map(int, elf_1.split('-'))
    elf_2_start, elf_2_end = map(int, elf_2.split('-'))

    if check_if_inside(elf_1_start, elf_1_end, elf_2_start, elf_2_end) or check_if_inside(elf_2_start, elf_2_end, elf_1_start, elf_1_end):
        count += 1

print(count)







