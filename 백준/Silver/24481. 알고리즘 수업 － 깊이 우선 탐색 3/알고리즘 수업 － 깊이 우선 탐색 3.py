# 입력
# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 
# 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)] 

# 인접리스트 생성
# 다음 M개 줄에 간선 정보 u v
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접정점은 오름차순!으로 방문한다
for line in graph:
    line.sort() 

# 미방문 노드 -1 표기
d = [-1] * (N+1) 

def dfs(depth, node):
    d[node] = depth
    for i in graph[node]: 
        if d[i] == -1:  
            dfs(depth+1, i)
    

# 출력
dfs(0, R)
print('\n'.join(map(str, d[1:])))