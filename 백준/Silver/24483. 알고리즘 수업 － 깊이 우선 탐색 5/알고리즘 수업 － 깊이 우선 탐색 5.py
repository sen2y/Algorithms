import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph: node.sort() # 오름차순
depth = [-1 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = 1
def dfs(node, d):
    global cnt
    visited[node] = cnt
    cnt+=1
    depth[node] = d
    for i in graph[node]: 
        if depth[i] == -1: dfs(i, d+1)
dfs(R, 0) 
 
total = sum(depth[i]*visited[i] for i in range(1,N+1))
print(total)
