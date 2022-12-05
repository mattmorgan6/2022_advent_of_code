import sys

file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()

crate_lines = []
num_bins = 0

i = 0
while i < len(lines):
    line_str = lines[i]
    if "[" in line_str:
        crate_lines.append(line_str)
    else:
        nums = line_str.split()
        num_bins = int(nums[-1])
        i += 2
        break

    i += 1

bins = [[] for _ in range(num_bins)]

for j in range(len(crate_lines) - 1, -1, -1):
    crate_line = crate_lines[j]
    # [Z] [M] [P]
    # 0123456789
    # chars are spaced out by 4 characters

    for k in range(num_bins):
        idx = (k * 4) + 1
        if idx < len(crate_line):
            c = crate_line[idx]
            if c != " ":
                bins[k].append(c)

# Store moves as "move [0] from [1] to [2]"
movements = []

while i < len(lines):
    line_str = lines[i].strip()
    tokens = line_str.split()
    movements.append((int(tokens[1]), int(tokens[3]), int(tokens[5])))

    i += 1

# Do the actual crane moving bins part.
for a, b, c in movements:
    for x in range(a):
        item = bins[b-1].pop()
        bins[c-1].append(item)

# print(bins)

for bin in bins:
    print(bin[-1], end='')

print()

