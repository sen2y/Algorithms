# 입력: 첫째줄에 R * C 칸, N초
import sys
# from collections import deque
input = sys.stdin.readline
R, C, N = map(int, input().split()) 

# 좌표 저장
grid = [list(input().strip()) for _ in range(R)]
# grid = [input().strip() for _ in range(R)]
# print(grid)

# # 모든 좌표가 폭탄이 심어진 경우
# all = [['O']*C for _ in range(R)]
# print(all)


# 과정: 폭탄이 있는 칸은 3초뒤 폭발, 인접한 상하좌우 네칸도 함께 파괴
# 인접한 폭탄은 폭발없이 파괴만 된다. 연쇄반응없다.
def bomb(grid):
    # 모든 좌표가 폭탄이 심어진 경우
    all = [['O']*C for _ in range(R)]
    # 현재 좌표에서 폭탄이 있는경우, all에서 grid 해당하는 상화좌우 포함해서 '.'로 변경하기
    # bfs일것같아 너비우선
    # q = deque([(0,0)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for cy in range(R):
        for cx in range(C): 
            if grid[cy][cx] == 'O': 
                # q.append((x,y))
            # while q:
                # x, y = q.popleft()
                # all에서 grid 해당하는 상화좌우 포함해서 '.'로 변경하기
                all[cy][cx] = '.'
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    # if 0<=nx<C and 0<=ny<R and grid[ny][nx]=='O': all[y][x] = '.'
                    if 0<=nx<C and 0<=ny<R: all[ny][nx] = '.'
    return all


# 0초: 초기 폭탄 설치 
# 1초: 아무것도안함
# 2초: 모든칸 폭탄 설치 
# 3초: 1초 시기의 폭탄 터짐. 
# 4초: 모든칸 폭탄 설치
# 5초: 3초에 설치했던 폭탄 터짐
# 6초: 모든칸 폭탄 설치
# 7초: 5초에 설치했던 폭탄 터짐

result = []

# 1,2초: 초기 폭탄
if N == 0 or N == 1: 
    result = grid
    # return
# 나머지 0, 2인경우 -> 모든 격자판 폭탄 설치
elif N % 4 == 0 or N % 4 == 2:   
    result = [['O'] * C for _ in range(R)]  
# 나머지 1, 3인경우 폭탄 터짐
# 나머지 1인경우 : 
elif N % 4 == 3: 
    result = bomb(grid)
# 나머지 3인경우 : 
elif N % 4 == 1:
    result = bomb(bomb(grid))
    # for i in second:
    #     result.append(''.join(i))
# 출력: N초가 지난 후의 격자판 상태를 출력하라
for row in result:
    print(''.join(row))
