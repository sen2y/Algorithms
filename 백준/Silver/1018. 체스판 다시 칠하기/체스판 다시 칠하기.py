import sys
input = sys.stdin.readline

 
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

min_repaint = float('inf')  # 아주 큰 값으로 초기화

# 모든 가능한 8×8 시작 위치
for i in range(N - 7):
    for j in range(M - 7):
        cntW = 0  # 왼쪽 위를 'W'로 시작할 때
        cntB = 0  # 왼쪽 위를 'B'로 시작할 때
        
        for x in range(8):
            for y in range(8):
                current = board[i + x][j + y]
                # (x + y) 짝수 위치는 시작 색, 홀수 위치는 반대 색
                if (x + y) % 2 == 0:
                    if current != 'W': cntW += 1
                    if current != 'B': cntB += 1
                else:
                    if current != 'B': cntW += 1
                    if current != 'W': cntB += 1
        
        # 이 구역에서의 최소 칠하기 횟수로 갱신
        min_repaint = min(min_repaint, cntW, cntB)

print(min_repaint)

 