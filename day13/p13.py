import ast
from functools import cmp_to_key
# x = ast.literal_eval(x)

def parse_input():
    lines = list(map(lambda e: e.strip(), open('p13.txt', 'r').readlines()))
    pairs = []
    for i in range(0, len(lines), 3):
        pairs.append([ast.literal_eval(lines[i]), ast.literal_eval(lines[i+1])])
    return pairs

def recur1(left, right) -> int:
    if not left and not right:
        return 0
    elif not left:
        return 1
    elif not right:
        return -1

    for i in range(len(left)):
        if i == len(right):
            # If right is shorter than left, return out of order
            return -1
        l, r = left[i], right[i]
        if type(l) is int and type(r) is int:
            # 2 ints, compare directly, only continue is eq
            if l < r:
                return 1
            elif r < l:
                return -1
        else:
            # 1 of 2 lists, recurse
            result = recur1(l if type(l) is list else [l], r if type(r) is list else [r])
            if result != 0:
                return result
    # if left is smaller than right, return in order, else undetermined
    if len(left) < len(right):
        return 1
    return 0

    

def part1():
    pairs = parse_input()
    sum = 0

    # Iterate and sum the idxs of the in order pairs
    for i in range(len(pairs)):
        sum += (1+i) if recur1(pairs[i][0], pairs[i][1]) == 1 else 0
    return sum

def part2():
    # destructure the pairs
    pairs = parse_input()
    packets = [[[2]], [[6]]]
    for pair in pairs:
        packets += pair

    # sort and reverse the result (due to choosing wrong sort results :( )
    packets.sort(key=cmp_to_key(recur1))
    packets.reverse()

    # Find the decoder signals
    d1, d2 = None, None
    for i in range(len(packets)):
        if packets[i] == [[2]]:
            d1 = i+1
        elif packets[i] == [[6]]:
            d2 = i+1
    
    # take product of decoder signals!
    return d1 * d2


print(part1())
print(part2())
