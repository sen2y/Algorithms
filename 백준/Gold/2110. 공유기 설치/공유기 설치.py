# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에\
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
xs = sorted([int(input()) for _ in range(N)])

low, high = 1, xs[-1] - xs[0]
res = 0

while low<=high:
    mid = (low+high) // 2
    cnt = 1
    last = xs[0]
    for i in range(1, N):
        if xs[i]-last >= mid:
            cnt +=1
            last = xs[i]
            if cnt>= C:  
                break
    if cnt >= C: 
        res = mid
        low = mid+1
    else:
        high = mid-1
print(res)