import sys
input = sys.stdin.readline

N = int(input()) # 지도의 크기
graph = [list(map(int, input().strip())) for _ in range(N)]

sizes = [] # 단지별 집의 수 

# dfs가 적합할 것 같다.
stack = []
visited = [[False]*N for _ in range(N)] 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def in_range(x, y):
    return 0<=x<N and 0<=y<N 

def dfs(px, py):
    stack.append((px,py))
    visited[py][px] = True
    size = 1

    while stack:
        nx, ny = stack.pop()
        for i in range(4):
            x, y = nx+dx[i], ny+dy[i]
            # 벽에 부딪히는가?
            if not in_range(x, y): continue 
            # 방문한적 있는가?
            if visited[y][x]: continue
            # 집이 존재하는가? 1인가
            if graph[y][x] == 1: 
                # 방문처리 
                visited[y][x] = True
                stack.append((x,y))
                size+=1
    return size



for y in range(N):
    for x in range(N):
        if not visited[y][x] and graph[y][x] == 1:
            sizes.append(dfs(x, y))

print(len(sizes))
print('\n'.join(map(str,sorted(sizes))))


        
