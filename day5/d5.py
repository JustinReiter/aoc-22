from typing import List, Tuple

def parse_input() -> Tuple[List[List[str]], List[List[int]]]:
    lines = open('p5.txt', 'r').readlines()

    stacks = [[] for _ in range(9)]
    for i in range(7, -1, -1):
        for ridx in range(9):
            if lines[i][ridx*4+1] != ' ':
                stacks[ridx].append(lines[i][ridx*4+1])

    rules = []
    for i in range(10, len(lines)):
        tokens = lines[i].split(' ')
        rules.append([int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1])
    return stacks, rules

def p1() -> str:
    stacks, rules = parse_input()
    for rule in rules:
        for _ in range(rule[0]):
            if not len(stacks[rule[1]]):
                break
            stacks[rule[2]].append(stacks[rule[1]].pop())
    ans = ""
    for stack in stacks:
        ans += stack[-1]
    return ans

def p2() -> str:
    stacks, rules = parse_input()
    for rule in rules:
        for i in range(rule[0]):
            stacks[rule[2]].append(stacks[rule[1]][-rule[0]+i])
        for _ in range(rule[0]):
            stacks[rule[1]].pop()
    ans = ""
    for stack in stacks:
        ans += stack[-1]
    return ans

print(p2())
