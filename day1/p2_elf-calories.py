from heapq import heappush, heappop, nlargest

lines = open('p1_elf-calories.input', 'r')
heap, current = [], 0
for line in lines:
    if line == '\n':
        heappush(heap, current)
        current = 0
    else:
        current += int(line)
if current:
    heappush(heap, current)

print(nlargest(3, heap))
print(sum(nlargest(3, heap)))
