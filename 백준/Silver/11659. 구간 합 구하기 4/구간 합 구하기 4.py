import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
ijs = [list(map(int, input().split())) for _ in range(M)]
# print(ijs)

dp = [0] * N
dp[0] = nums[0]
for k in range(1,N):
    dp[k] = dp[k-1] + nums[k]
# print(dp)
for i, j in ijs:
    if i==j: print(nums[i-1])
    elif i==1: print(dp[j-1])
    else: print(dp[j-1]- dp[i-2]) 

