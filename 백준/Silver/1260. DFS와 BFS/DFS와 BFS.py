# from collections import deque
# import sys
# input = sys.stdin.read

# data = input().rstrip().split('\n')
# # 정점 개수 N, 간선 개수 M, 탐색 시작 정점 번호 V
# n, m, v = map(int, data[0].split())
# data = data[1:]

# # 인덱스 0 무시
# graph = [[] for i in range(n+1)] 
# # print(graph)
# # 좌표 생성
# for i in range(m):
#     a, b = map(int, data[i].split())
#     graph[a].append(b)
#     graph[b].append(a)
# # print(graph)
# # 정점 번호가 작은것부터 방문이므로 오름차순 정렬
# for adj in graph:
#     adj.sort() 


# def dfs(graph, node, visited): 
#     # 재귀
#     for i in graph[node]:
#         if i not in visited:
#             visited.append(i)
#             dfs(graph, i, visited)
#     return visited

# def bfs(graph, node):
#     # 큐
#     visited = [node]
#     q = deque([node])
#     while q:
#         cur = q.popleft()
#         for i in graph[cur]:
#             if i not in visited:
#                 visited.append(i)
#                 q.append(i)
#     return visited


    

# print(' '.join(map(str, dfs(graph, v, [v]))))
# print(' '.join(map(str, bfs(graph, v))))

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V
import sys 
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# print(visited)
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for list in graph: list.sort()
# print(graph)

def dfs(start): # 스택  
    visited = [False] * (N+1)
    stack = [start]
    # print(start) 
    result = []

    while stack:
        node = stack.pop()
        if not visited[node]: 
            visited[node] = True
            # print(node)
            result.append(node)
            for v in reversed(graph[node]):
                if not visited[v]: 
                    # print(v,999)
                    # visited[v] = True
                    stack.append(v)
    return result

def bfs(start): # 큐
    visited = [False] * (N+1)
    q = deque([start])
    visited[start] =True
    result = []

    while q:
        node = q.popleft()
        result.append(node)
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return result



# 정점 번호가 작은 것을 먼저 방문 (오름차순 )
# 더 이상 방문할 수 있는 점이 없는 경우 종료

# 첫째 줄에 DFS, 그 다음 줄에는 BFS
print(' '.join(map(str,dfs(V))))
print(' '.join(map(str,bfs(V))))









