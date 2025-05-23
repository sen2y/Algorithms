# 덱
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

q = deque()
for _ in range(N):
    line = list(input().split())
    order = line[0] 
    if order == 'push_front': q.appendleft(line[1])
    if order == 'push_back': q.append(line[1])
    elif order == 'pop_front': print(q.popleft() if len(q)>0 else -1)
    elif order == 'pop_back':  print(q.pop() if len(q)>0 else -1)
    elif order == 'size': print(len(q))
    elif order == 'empty': print(0 if len(q)>0 else 1)
    elif order == 'front': print(q[0] if len(q)>0 else -1)
    elif order == 'back': print(q[-1] if len(q)>0 else -1)