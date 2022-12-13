lines = open('p1.input', 'r').read().splitlines()



sum = 0
for idx in range(0, len(lines), 3):
    s1, s2, s3 = set(list(lines[idx])), set(list(lines[idx+1])), set(list(lines[idx+2]))
    inters = s1.intersection(s2).intersection(s3).pop()

    if ord(inters) > 96:
        sum += ord(inters) - 96
    else:
        sum += ord(inters) - 64 + 26

print(sum)

