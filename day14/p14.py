

from typing import List


def parse_input():
    return list(map(lambda e: e.strip().split(' -> '), open('p14.txt', 'r').readlines()))
    # return list(map(lambda e: e.strip().split(' -> '), open('p14i.test', 'r').readlines()))

def max_depth():
    lines = parse_input()
    depth = 0
    for line in lines:
        for part in line:
            y = int(part.split(',')[1])
            depth = max(depth, y)
    return depth

def build_board() -> List[List[str]]:
    lines = parse_input()
    board = [['.']*169 for _ in range(1000)]
    
    # build the board
    for line in lines:
        # parse each line:
        for i in range(1, len(line)):
            x1, y1 = map(lambda e: int(e), line[i-1].split(','))
            x2, y2 = map(lambda e: int(e), line[i].split(','))

            if x1 == x2:
                # difference is vertical
                if y1 > y2:
                    # WLOG
                    y1, y2 = y2, y1
                for j in range(y1, y2+1):
                    board[x1][j] = '#'
            else:
                # difference is vertical
                if x1 > x2:
                    # WLOG
                    x1, x2 = x2, x1
                for i in range(x1, x2+1):
                    board[i][y1] = '#'
    return board

def simulate(board: List[List[str]], with_floor: bool):
    sands = 0
    while True:
        new_sand = [500, 0]
        does_settle = True
        while True:
            if new_sand[1]+1 >= len(board[0]) and with_floor:
                # new sand cannot drop down a row and a floor exists (sand should settle)
                break
            elif new_sand[1]+1 >= len(board[0]):
                # new sand cannot drop down a row and enters the abyss
                does_settle = False
                break

            if board[new_sand[0]][new_sand[1]+1] == '.':
                # down
                new_sand[1] += 1
            elif board[new_sand[0]-1][new_sand[1]+1] == '.':
                # diag left
                new_sand[0] -= 1
                new_sand[1] += 1
            elif board[new_sand[0]+1][new_sand[1]+1] == '.':
                # diag right
                new_sand[0] += 1
                new_sand[1] += 1
            else:
                # uh oh, cannot drop a row
                break
        if does_settle:
            # sand settles, keep iterating (unless we reach the starting point during part 2)
            sands += 1
            board[new_sand[0]][new_sand[1]] = 'o'
            if new_sand[0] == 500 and new_sand[1] == 0:
                break
        else:
            # sand reaches the abyss, stop iterating
            break
    return sands

def print_board(board):
    # print board to view
    output_str = ''
    for y in range(len(board[0])):
        for x in range(len(board)):
            output_str += board[x][y]
        output_str += '\n'
    print(output_str)


def part1():
    board = build_board()

    # simulate without a floor
    return simulate(board, False)


def part2():
    board = build_board()
    # print_board(board)

    # simulate with a floor
    return simulate(board, True)

print(max_depth())
print(part1())
print(part2())
