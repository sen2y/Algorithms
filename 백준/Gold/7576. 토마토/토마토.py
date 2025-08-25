import sys
from collections import deque
input = sys.stdin.readline

# 첫 줄에는 상자의 크기를 나타내는 두 정수 가로 M, 세로 N (2 ≤ M,N ≤ 1,000)
# 둘째줄부터, 하나의 상자에 저장된 토마토들의 정보
# 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    return 0<=x<M and 0<=y<N

#  보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 최단거리같다. 가중치 없는 그래프의 최단거리 bfs!
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
def bfs(): 
    while q:
        sx, sy = q.popleft()
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if in_range(nx, ny) and graph[ny][nx]==0 : 
                graph[ny][nx] = graph[sy][sx] + 1
                q.append((nx, ny))
                


# 토마토가 모두 익을 때까지의 최소 날짜
q = deque()
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1: 
            q.append((x,y))
bfs()
            
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1
res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit(0)
        res = max(res, j)
        
print(res-1)

