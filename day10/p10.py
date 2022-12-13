
def parse_input():
    return list(map(lambda e: e.strip(), open('p10.txt', 'r').readlines()))

def parse_test2():
    return list(map(lambda e: e.strip(), open('p10ii.test', 'r').readlines()))

def part1():
    X = 1
    cycle = 0
    lines = parse_input()
    sig_str = []
    output = [X]

    for line in lines:
        if line[0:4] == 'noop':
            # noop
            cycle += 1
            if (cycle + 20) % 40 == 0:
                sig_str.append(cycle * X)
            output.append(X)
        else:
            # addx
            cycle += 1
            output.append(X)
            if (cycle + 20) % 40 == 0:
                sig_str.append(cycle * X)
            cycle += 1
            if (cycle + 20) % 40 == 0:
                sig_str.append(cycle * X)
            X += int(line[5:])
            output.append(X)
    return sum(sig_str), output
        


def part2(Xs):
    output_str = ''
    for i in range(241):
        if i % 40 == 0 and i != 0:
            output_str += '\n'
        
        # add row
        if abs((Xs[i]) - (i%40)) <= 1:
            output_str += '#'
        else:
            output_str += '.'
    return output_str

ans, output = part1()
print(part2(output))
