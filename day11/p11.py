

from collections import deque
import math
from typing import List

global lcm_all
def parse_input(should_div):
    lines = list(map(lambda e: e.strip(), open('p11.txt', 'r').readlines()))

    monkeys: List[Monkey] = []
    for line in lines:
        if line.startswith('Monkey'):
            monkeys.append(Monkey(should_div))
        elif line.startswith('Starting'):
            monkeys[-1].q.extend(list(map(lambda e: int(e), line[16:].split(', '))))
        elif line.startswith('Operation'):
            tokens = line.split(' ')
            monkeys[-1].op = tokens[4]
            monkeys[-1].end = tokens[5]
        elif line.startswith('Test'):
            monkeys[-1].test_val = int(line.split(' ')[3])
        elif line.startswith('If true'):
            monkeys[-1].goto[True] = int(line.split(' ')[5])
        elif line.startswith('If false'):
            monkeys[-1].goto[False] = int(line.split(' ')[5])
    global lcm_all
    lcm_all = math.lcm(*list(map(lambda e: int(e.test_val), monkeys)))
    return monkeys

class Monkey:
    def __init__(self, should_div):
        self.q = deque()
        self.insps = 0
        self.op = None
        self.end = None
        self.op_val = None
        self.test_val = None
        self.goto = {
            True: None,
            False: None
        }
        self.should_div = should_div
    
    def inspect(self, monkeys: List['Monkey']):
        while self.q:
            new_item = self.q.popleft()
            new_item = self.operation(new_item)
            if self.should_div:
                new_item = new_item // 3
            monkeys[self.goto[self.test(new_item)]].q.append(new_item % lcm_all)
            self.insps += 1
    
    def test(self, val):
        return val % self.test_val == 0

    def operation(self, result):
        if self.op == '*':
            if self.end == 'old':
                return result ** 2
            else:
                return result * int(self.end)
        else:
            if self.end == 'old':
                return result * 2
            else:
                return result + int(self.end)

def part1():
    monkeys = parse_input(True)

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect(monkeys)
    
    # test
    vals = list(map(lambda e: e.insps, monkeys))
    print(vals)
    vals.sort()
    return vals[-2] * vals[-1]
    

def part2():
    monkeys = parse_input(False)

    for _ in range(10_000):
        for monkey in monkeys:
            monkey.inspect(monkeys)
    
    # test
    vals = list(map(lambda e: e.insps, monkeys))
    print(vals)
    vals.sort()
    return vals[-2] * vals[-1]


print(part1())
print(part2())
