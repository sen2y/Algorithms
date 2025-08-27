# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M
# 둘째 줄에는 나무의 높이

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hs = list(map(int, input().split()))

low, high = 1, max(hs)
res = 0
while low<=high:
    cnt = 0
    mid = (low+high)//2
    for h in hs:
        if h>mid:
            cnt+=h-mid
            if cnt>=M: break
    if cnt>=M:
        res = mid
        low = mid+1
    else: high = mid-1

print(res)

        