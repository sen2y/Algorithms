import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    line = input().strip()
    if line.startswith('push'):
        _, n = line.split()
        q.append(n)
    elif line == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif line == 'size': 
        print(len(q))
    elif line == 'front':
        if q: print(q[0])
        else: print(-1)
    elif line == 'back':
        if q: print(q[-1])
        else: print(-1)
    elif line == 'empty':
        print(0 if q else 1)




