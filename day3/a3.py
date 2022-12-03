import sys

file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()

results = []
for line_str in lines:
    line = line_str.strip()

    split_point = len(line) // 2
    first_pack, second_pack = set(line[:split_point]), set(line[split_point:])
    intersection = first_pack.intersection(second_pack)
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





