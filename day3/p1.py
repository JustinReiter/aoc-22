lines = open('p1.input', 'r')

sum = 0
for line in lines:
    line = line.replace('\n', '')
    halfway = len(line)//2
    matches = set(list(line[0:halfway])).intersection(set(list(line[halfway:]))).pop()

    for match in matches:
        if ord(match) > 96:
            sum += ord(match) - 96
        else:
            sum += ord(match) - 64 + 26
            
print(sum)
