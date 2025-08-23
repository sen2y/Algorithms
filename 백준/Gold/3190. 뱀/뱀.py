import sys
from collections import deque
input = sys.stdin.readline
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 
# 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
N = int(input())
K = int(input())

#  K개의 줄에는 사과의 위치가 주어지는데, 
# 사과의 위치는 모두 다르며, (1행 1열) 에는 사과가 없다.
apples = set()
for _ in range(K):
# 첫 번째 정수는 행, 두 번째 정수는 열 의미
    r, c = map(int, input().split())
    # 나는 x,y축 기준으로 할거니까, c,r로 저장해야한다.
    apples.add((c,r))

# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
L = int(input())
# 다음 L개의 줄에는 방향변환정보가 주어진다.
dirs = deque()
for _ in range(L):
# 정수 X와 문자 C, 
# 방향 전환 정보는 X가 증가하는 순으로 주어진다.
    X, C = input().split()
    dirs.append((int(X), C))
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L'), 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.

# 초기방향 dir=0, (1,1)에서 시작
dir = 0
loc = deque([(1,1)]) # deque((1,1))로 하면 튜플로 저장안된다.
dx = [1, 0, -1, 0] # 동 남 서 북
dy = [0, 1, 0, -1] # 좌표기준이니까 x,y축이어도 내려갈때 y값 증가

def out_of_range(x, y):
    return 1 if 0>=x or x>N or 0>=y or y>N else 0

sec = 1
while True: 
    x, y = loc[-1]
    x, y = x + dx[dir], y + dy[dir] 
    
    # 1. 벽에 부딪히면
    if out_of_range(x, y): 
        print(sec)
        break;

    # 2. 자기몸에 부딪히면 (사과먹는경우는 제외)
    # 사과없는칸이고, 꼬리랑 겹치는 경우는 제외
    has_apple = (x, y) in apples
    if has_apple and (x, y) in loc:
        print(sec)
        break
    elif not has_apple and (x,y) in list(loc)[:-1]:
        print(sec)
        break
        
    # 3. 사과 여부 확인
    # 사과 있으면 apples에서 제거하고, 좌표 추가
    loc.append((x,y))
    if has_apple: 
            apples.remove((x,y))
    # 사과 없으면 좌표 추가 및 꼬리 제거
    else: 
        loc.popleft()

    if dirs and sec == dirs[0][0]:
        X, C = dirs.popleft()
        if C == 'D': dir = (dir +1)%4
        else: dir = (dir+3)%4
    sec+=1




