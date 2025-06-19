import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# 내림차순으로 방문
for node in graph: node.sort(reverse = True)

visited = [0] * (N+1)
def bfs(R):
    cnt = 1
    q = deque([R])
    visited[R] = cnt
    cnt += 1
    while q:
        node = q.popleft() 
        for n in graph[node]:
            if visited[n] == 0: 
                visited[n] = cnt
                cnt +=1
                q.append(n)
bfs(R)
print('\n'.join(map(str,visited[1:])))

