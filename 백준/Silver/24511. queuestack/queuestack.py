import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))  # 자료구조 타입: 0은 큐, 1은 스택
B = list(map(int, input().split()))  # 각 자료구조에 초기로 들어있는 값
M = int(input())
C = list(map(int, input().split()))  # 삽입할 값들

# 0번 타입(큐)인 자료구조들의 초기값만 역순으로 deque에 저장
dq = deque()
result = []

for i in range(N - 1, -1, -1):  # 역순으로
    if A[i] == 0:
        dq.append(B[i])

# 새로운 값 삽입하고 맨 앞 값을 pop해서 출력
for x in C:
    dq.append(x)
    result.append(dq.popleft())

print(' '.join(map(str, result)))