import sys
from collections import deque
input = sys.stdin.read

n = int(input())
def solution(n):
    q = deque([i+1 for i in range(n)]) 
    while len(q)>1:
        q.popleft()
        a = q.popleft()
        q.append(a)
    
    print(q.pop())
    

solution(n)