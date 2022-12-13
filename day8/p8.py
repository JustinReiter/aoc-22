
def parse_input():
    return list(map(lambda e: e.strip(), open('p8.txt', 'r').readlines()))

def part1():
    grid = parse_input()
    visible_trees = 0

    for ridx, row in enumerate(grid):
        for cidx, cell in enumerate(row):
            if ridx == 0 or ridx+1 == len(grid) or cidx == 0 or cidx+1 == len(row):
                # exterior
                visible_trees += 1
            else:
                # check if visible
                is_visible = True
                for i in range(0, ridx):
                    # columns
                    if grid[i][cidx] >= cell:
                        is_visible = False
                        break
                if is_visible:
                    visible_trees += 1
                    continue
                
                is_visible = True
                for i in range(ridx+1, len(grid)):
                    # columns
                    if grid[i][cidx] >= cell:
                        is_visible = False
                        break
                if is_visible:
                    visible_trees += 1
                    continue

                is_visible = True
                for i in range(0, cidx):
                    # columns
                    if row[i] >= cell:
                        is_visible = False
                        break
                if is_visible:
                    visible_trees += 1
                    continue

                is_visible = True
                for i in range(cidx+1, len(row)):
                    # columns
                    if row[i] >= cell:
                        is_visible = False
                        break
                if is_visible:
                    visible_trees += 1
                    continue
    return visible_trees

                

def part2():
    grid = parse_input()

    best = 0
    for ridx in range(0, len(grid)):
        for cidx in range(0, len(grid[ridx])):
            # find viewing angle
            prod, cur = 1, 0

            for i in range(ridx-1, -1, -1):
                cur += 1
                if grid[i][cidx] >= grid[ridx][cidx]:
                    break
            prod *= cur
            cur = 0
            for i in range(ridx+1, len(grid)):
                cur += 1
                if grid[i][cidx] >= grid[ridx][cidx]:
                    break
            
            prod *= cur
            cur = 0
            for i in range(cidx-1, -1, -1):
                cur += 1
                if grid[ridx][i] >= grid[ridx][cidx]:
                    break
            prod *= cur
            cur = 0
            for i in range(cidx+1, len(grid[ridx])):
                cur += 1
                if grid[ridx][i] >= grid[ridx][cidx]:
                    break
            prod *= cur
            best = max(best, prod)
    return best



print(part1())
print(part2())