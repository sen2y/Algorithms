from collections import deque
import sys
input = sys.stdin.read

data = input().rstrip().split('\n')
# 정점 개수 N, 간선 개수 M, 탐색 시작 정점 번호 V
n, m, v = map(int, data[0].split())
data = data[1:]

# 인덱스 0 무시
graph = [[] for i in range(n+1)] 
# print(graph)
# 좌표 생성
for i in range(m):
    a, b = map(int, data[i].split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
# 정점 번호가 작은것부터 방문이므로 오름차순 정렬
for adj in graph:
    adj.sort() 


def dfs(graph, node, visited): 
    for j in graph[node]:
        if j not in visited: 
            visited.append(j) 
            dfs(graph, j, visited) 
    return visited


def bfs(graph, node):
    # 시작 노드 visited, q에 초기화
    visited = [node]
    q = deque([node])
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            # 방문하지 않은 노드만 visited, q에 추가
            if i not in visited: 
                visited.append(i) 
                q.append(i)
    return visited
    

print(' '.join(map(str, dfs(graph, v, [v]))))
print(' '.join(map(str, bfs(graph, v))))