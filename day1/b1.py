import sys
import heapq

file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()

    heap = []

    elf_cals = 0
    for l in lines:
        line = l.strip()
        if len(line) == 0:
            if len(heap) >= 3:
                heapq.heappushpop(heap, elf_cals)
            else:
                heapq.heappush(heap, elf_cals)
            elf_cals = 0
        else:
            num = int(line)
            elf_cals += num

    # In case there isn't a blank line after the last value in the file:
    if len(heap) >= 3:
        heapq.heappushpop(heap, elf_cals)
    else:
        heapq.heappush(heap, elf_cals)
        elf_cals = 0

    print(heap)
    print(sum(heap))


