# 입력
import sys
input = sys.stdin.readline
from collections import deque

# 입력의 첫째 줄에는 현재 승환이의 앞에 서 있는 학생들의 수 N(1 ≤ N ≤ 1,000,자연수)
N = int(input()) 
# 다음 줄에는 승환이 앞에 서있는 모든 학생들의 번호표(1,2,...,N) 순서
q = deque(list(map(int, input().split())))
stack = []
cnt = 1

while q or stack:
    # q가 있으면 
    if q and q[0] == cnt:
        q.popleft()
        cnt += 1
    elif stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
    elif q:
        stack.append(q.popleft())
    else:
        break
         
             
# 출력
# 승환이가 무사히 간식을 받을 수 있으면 "Nice"
# 그렇지 않다면 "Sad"
print("Nice" if cnt == N+1 else "Sad")