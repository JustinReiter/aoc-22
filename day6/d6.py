
from collections import deque

def read_input():
    return open('p6.txt', 'r').readlines()[0].strip()

def p1():
    msg = read_input()

    q = deque(list(msg[0:4]))
    if len(set(q)) == 4:
        return 4
    for i in range(4, len(msg)):
        q.popleft()
        q.append(msg[i])
        if len(set(q)) == 4:
            return i+1

def p2(N):
    msg = read_input()

    q = deque(list(msg[0:N]))
    print(q)
    if len(set(q)) == N:
        return N
    for i in range(N, len(msg)):
        q.popleft()
        q.append(msg[i])
        if len(set(q)) == N:
            print(q)
            return i+1
    
print(p1())
print(p2(14))


