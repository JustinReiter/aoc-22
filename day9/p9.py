from typing import List


def parse_input():
    return list(map(lambda e: e.strip(), open('p9.txt', 'r').readlines()))

def parse_test():
    return list(map(lambda e: e.strip(), open('p9i.test', 'r').readlines()))

def parse_test2():
    return list(map(lambda e: e.strip(), open('p9ii.test', 'r').readlines()))

def update_unit(h, t):
    # update tail if needed
    dx, dy = abs(h[0] - t[0]), abs(h[1] - t[1])
    if dx > 1:
        # two units away laterally
        t[0] += 1 if (h[0] - t[0]) > 0 else -1
        if dy >= 1:
            # one unit vertical
            t[1] += 1 if (h[1] - t[1]) > 0 else -1
    elif dy > 1:
        # two units away vertically
        t[1] += 1 if (h[1] - t[1]) > 0 else -1
        if dx >= 1:
            # one unit horizontal
            t[0] += 1 if (h[0] - t[0]) > 0 else -1
    return t


def part1():
    lines = parse_input()

    pos = set()
    pos.add(tuple([0, 0]))
    h, t = [0, 0], [0, 0]

    for line in lines:
        for _ in range(int(line[2:])):
            # update head according to line
            match line[0]:
                case 'U':
                    h[1] += 1
                case 'R':
                    h[0] += 1
                case 'D':
                    h[1] -= 1
                case 'L':
                    h[0] -= 1
            
            t = update_unit(h, t)
            pos.add(tuple(t))
    return len(pos)

def print_end_grid(seen):
    output_str = ''
    for y in range(20):
        for x in range(40):
            if tuple([x-20, y-10]) in seen:
                output_str += '#'
            else:
                output_str += '.'
        output_str += '\n'
    rev_out = output_str.split('\n')
    rev_out.reverse()
    print('\n'.join(rev_out))

def print_grid(stack: List):
    output_str = ''
    for y in range(20):
        for x in range(40):
            idx = stack.index([x-20, y-10]) if [x-20, y-10] in stack else -1
            if idx >= 0:
                output_str += '{}'.format(idx if idx > 0 else 'H')
            else:
                output_str += '.'
        output_str += '\n'
    rev_out = output_str.split('\n')
    rev_out.reverse()
    print('\n'.join(rev_out))
            
def part2():
    lines = parse_input()

    pos = set()
    pos.add(tuple([0, 0]))
    stack = [[0, 0] for _ in range(10)]

    for line in lines:
        for _ in range(int(line[2:])):
            # update head according to line
            match line[0]:
                case 'U':
                    stack[0][1] += 1
                case 'R':
                    stack[0][0] += 1
                case 'D':
                    stack[0][1] -= 1
                case 'L':
                    stack[0][0] -= 1
            
            # update knots
            for knot_idx in range(1, len(stack)):
                stack[knot_idx] = update_unit(stack[knot_idx-1], stack[knot_idx])
            # print_grid(stack)
            pos.add(tuple(stack[-1]))
    # print_end_grid(pos)
    return len(pos)


print(part1())
print(part2())
