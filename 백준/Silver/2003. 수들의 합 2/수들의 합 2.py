import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 연속된 수열의 합이 M이 되는 경우의수.
first, last = 0, 0
cnt = 0
res = 0

while True: 
    if cnt >= M:
        if cnt == M:
            res += 1
        cnt -= A[first]
        first += 1
    elif last == N: break
    else:
        cnt += A[last]
        last += 1


print(res)
