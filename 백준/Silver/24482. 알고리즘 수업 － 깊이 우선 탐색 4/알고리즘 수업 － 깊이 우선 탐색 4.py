# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)
# 다음 M개 줄에 간선 정보 u v
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = list(map(int, input().split())) 

graph = [[] for _ in range(N+1)]
depth = [-1 for _ in range(N+1)] 

for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
# 인접 정점은 내림차순으로 방문한다.
for i in graph: i.sort(reverse=True) 

def dfs(node, d): 
    depth[node] = d
    for k in graph[node]: 
        if depth[k] == -1: dfs(k, d+1)



# 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력
# i번째 줄에는 정점 i의 깊이를 출력
# 시작 정점 R의 깊이는 0이고 방문 되지 않는 노드의 깊이는 -1로 출력
dfs(R, 0)
print('\n'.join(map(str, depth[1:])))