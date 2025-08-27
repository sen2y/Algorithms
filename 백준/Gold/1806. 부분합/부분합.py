import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

fir, las = 0, 0
cnt = 0
res = float('inf') # min

while True:
    if cnt >= S: 
        res = min(res, las-fir)
        cnt -= A[fir]
        fir += 1
    elif las == N: break
    else:
        cnt += A[las]
        las += 1
print(0 if res == float('inf') else res)
        