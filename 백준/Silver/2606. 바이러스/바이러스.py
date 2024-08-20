def check():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    # print(graph)
    
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (n+1)

    def dfs(v):
        visited[v] = True
        for i in graph[v]:
            if not visited[i] : dfs(i)

    dfs(1)
    print(sum(visited)-1)

check()