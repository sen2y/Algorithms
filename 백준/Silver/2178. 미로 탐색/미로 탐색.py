# 미로에서 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
miros = [list(map(int,input().strip())) for _ in range(N)]
# 지나지 않은 칸은 -1
dist = [[-1]*M for _ in range(N)]
dist[0][0] = 1 # 첫번째 칸은 1로 시작
q = deque([(0,0)])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 1 if 0<=x<M and 0<=y<N else 0

# 값이 1일때만 접근 가능, 
# 최소의 칸 수를 출력 == 최단거리 요구. -> visited대신 dist[y][x]를 거리로 사용. 
# bfs는 큐를 이용, 시작점에서 가까운 칸부터 차례로 탐색. 어떤칸에 처음 도달할때 그칸까지의 경로는 가장 짧은 경로이다.

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 그래프 범위 안인가?
        if not in_range(nx, ny):
            continue
        # 방문했던 곳인가?
        if dist[ny][nx] != -1:
            continue
        # 미로 칸이 1인가?
        if miros[ny][nx] == 1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((nx, ny))


# output
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수
print(dist[N-1][M-1])