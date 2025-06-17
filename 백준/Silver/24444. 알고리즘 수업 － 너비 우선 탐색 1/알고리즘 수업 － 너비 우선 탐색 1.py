from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# 인접 정점은 오름차순으로 방문한다.
for node in graph: node.sort()

visited = [0] * (N+1)
cnt = 1

def bfs(start): 
    global cnt
    q = deque([start])
    visited[start] = cnt
    cnt +=1 
    while q: 
        node = q.popleft()
        for i in graph[node]: 
            if visited[i] == 0: 
                visited[i] = cnt
                cnt += 1
                q.append(i)

bfs(R)
print('\n'.join(map(str, visited[1:])))
