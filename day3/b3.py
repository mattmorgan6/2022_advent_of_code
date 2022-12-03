import sys

file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()

results = []
i = 0
while i < len(lines):

    packs = []
    for j in range(3):
        line = lines[i].strip()
        packs.append(set(line))
        i += 1

    assert len(packs) == 3
    intersection = packs[0].intersection(packs[1].intersection(packs[2]))
    # print(intersection)
    assert len(intersection) == 1
    results.append(intersection.pop())

priorities = []
for letter in results:
    if ord(letter) <= ord('Z'):
        # capital letter
        priorities.append(ord(letter) - ord('A') + 27)
    else:
        # lower case
        priorities.append(ord(letter) - ord('a') + 1)

print(sum(priorities))





