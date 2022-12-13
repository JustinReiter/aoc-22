from collections import deque

def parse_input():
    return list(map(lambda e: list(e.strip()), open('p12.txt', 'r').readlines()))
    # return list(map(lambda e: e.strip(), open('p12.txt', 'r').readlines()))
    # return list(map(lambda e: e.strip(), open('p12.txt', 'r').readlines()))

def dir_to_go(goal, cur):
    dy, dx = goal[0] - cur[0], goal[1] - cur[1]

    if dy > 0:
        if dx == 0:
            pass

def part1():
    grid = parse_input()
    q = deque()
    q.append([0, 20, 0])

    # Hard-code and change values so we can use ord()
    grid[20][0] = 'a'
    grid[20][91] = 'z'

    # Contains nodes we have visited (not nodes to visit in the q)
    seen = set()

    while q:
        steps, row, col = q.popleft()
        if row == 20 and col == 91:
            # reached the goal!
            return steps
        elif (row, col) in seen:
            continue
        seen.add((row, col))
        
        if row > 0 and ord(grid[row][col]) - ord(grid[row-1][col]) >= -1:
            # Move up
            q.append([steps+1, row-1, col])
        if row+1 < len(grid) and ord(grid[row][col]) - ord(grid[row+1][col]) >= -1:
            # Move down
            q.append([steps+1, row+1, col])
        if col > 0 and ord(grid[row][col]) - ord(grid[row][col-1]) >= -1:
            # Move left
            q.append([steps+1, row, col-1])
        if col+1 < len(grid[0]) and ord(grid[row][col]) - ord(grid[row][col+1]) >= -1:
            # Move right
            q.append([steps+1, row, col+1])
    raise Exception()

def part2():
    grid = parse_input()
    q = deque()
     # Hard-code and change values so we can use ord()
    grid[20][0] = 'a'
    grid[20][91] = 'z'

    # Contains nodes we have visited (not nodes to visit in the q)
    grid[20][91] = 'z'
    grid[20][0] = 'a'

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'a':
                q.append([0, row, col])

    seen = set()

    while q:
        steps, row, col = q.popleft()
        if row == 20 and col == 91:
            # reached the goal!
            return steps
        elif (row, col) in seen:
            continue
        seen.add((row, col))
        
        if row > 0 and ord(grid[row][col]) - ord(grid[row-1][col]) >= -1:
            # Move up
            q.append([steps+1, row-1, col])
        if row+1 < len(grid) and ord(grid[row][col]) - ord(grid[row+1][col]) >= -1:
            # Move down
            q.append([steps+1, row+1, col])
        if col > 0 and ord(grid[row][col]) - ord(grid[row][col-1]) >= -1:
            # Move left
            q.append([steps+1, row, col-1])
        if col+1 < len(grid[0]) and ord(grid[row][col]) - ord(grid[row][col+1]) >= -1:
            # Move right
            q.append([steps+1, row, col+1])
    raise Exception()


print(part1())
print(part2())
