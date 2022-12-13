lines = open('p1.input', 'r')

score = 0
win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

pts = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


for line in lines:
    line = line.replace('\n', '')
    opp, user = line.split(' ')
    if draw[opp] == user:
        # draw
        score += 3
    elif win[opp] == user:
        # win
        score += 6
    score += pts[user]

print(score)

