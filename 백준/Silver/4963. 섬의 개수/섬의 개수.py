import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, -1, 0, 1, 1, -1, -1, 1]

def in_range(x, y):
    return 0<=x<w and 0<=y<h

def dfs(x,y,visited):
    stack = [(x,y)]
    while stack:
        px, py = stack.pop()
        for i in range(8):
            nx, ny = px+dx[i], py+dy[i]
            if in_range(nx, ny) and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                stack.append((nx,ny))

while True:
    w, h = map(int, input().split())
    # 종료 조건
    if w==0 and h==0: break

    cnt = 0 # 섬의 개수
    graph = [list(map(int,input().split())) for _ in range(h)] 
    visited = [[False] * (w) for _ in range(h)]
    # print(graph)
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                dfs(x, y,visited)
                cnt += 1
    print(cnt)






