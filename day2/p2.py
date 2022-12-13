lines = open('p1.input', 'r')

score = 0
win = {
    'A': 2,
    'B': 3,
    'C': 1
}

draw = {
    'A': 1,
    'B': 2,
    'C': 3
}

lose = {
    'A': 3,
    'B': 1,
    'C': 2
}

pts = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


for line in lines:
    line = line.replace('\n', '')
    opp, outcome = line.split(' ')
    
    if outcome == 'X':
        # lose
        score += lose[opp]
    elif outcome == 'Y':
        # draw
        score += draw[opp] + 3
    else:
        # win
        score += win[opp] + 6

print(score)
