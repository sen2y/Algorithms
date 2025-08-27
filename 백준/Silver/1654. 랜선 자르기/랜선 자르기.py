# 오영식이 이미 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N (K ≦ N)
# K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

low, high = 1, max(lines) 

while low<=high:
    mid = (low+high)//2
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt >= N: 
        res = mid
        low = mid+1
    else: 
        high = mid-1

print(res)


