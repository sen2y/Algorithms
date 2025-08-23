import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque(range(1, N+1))

result = []
while q: 
    q.rotate(-K)
    result.append(q.pop())

print("<"+ ', '.join(map(str,result))+ ">")
