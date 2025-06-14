import sys
from collections import deque
input = sys.stdin.readline



N,M = list(map(int, input().split()))
targets = list(map(int, input().split()))
dq = deque(range(1, 1+N))

cnt = 0

for t in targets:
    idx = dq.index(t)
    if idx <= len(dq)//2:
        dq.rotate(-idx)
        cnt+= idx
    else: 
        dq.rotate(len(dq)-idx)
        cnt+= len(dq)-idx
    dq.popleft()

print(cnt)
