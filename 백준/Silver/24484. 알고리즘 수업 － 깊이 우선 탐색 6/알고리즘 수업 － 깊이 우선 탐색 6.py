import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
# 내림차순 방문
for node in arr: node.sort(reverse=True)

depth = [-1 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = 1
def dfs(node, d):
    global cnt
    depth[node] = d
    visited[node] = cnt
    cnt+=1
    for i in arr[node]:
        if depth[i] == -1: dfs(i, d+1)
    
dfs(R, 0) 

total = sum(depth[i]*visited[i] for i in range(1, N+1))
print(total)