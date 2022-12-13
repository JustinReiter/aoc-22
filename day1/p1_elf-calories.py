lines = open('p1_elf-calories.input', 'r')
best, current = 0, 0
for line in lines:
    if line == '\n':
        best, current = max(best, current), 0
    else:
        current += int(line)
print(max(current, best))
