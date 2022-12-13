lines = open('d4_i.input', 'r').read().splitlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].replace('\n', '')


def p1(lines: list[str]) -> int:
    overlaps = 0

    for line in lines:
        p1, p2 = line.split(',')
        
        l1, r1 = p1.split('-')
        l2, r2 = p2.split('-')

        if int(l2) >= int(l1) and int(r2) <= int(r1):
            overlaps += 1
        elif int(l1) >= int(l2) and int(r1) <= int(r2):
            overlaps += 1
    return overlaps

def p2(lines: list[str]) -> int:
    overlaps = 0

    for line in lines:
        p1, p2 = line.split(',')
        
        l1, r1 = map(lambda a: int(a), p1.split('-'))
        l2, r2 = map(lambda a: int(a), p2.split('-'))

        if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
            overlaps += 1

    return overlaps

print(p2(lines))
