import sys
input = sys.stdin.readline

T = int(input())
ns = [int(input()) for _ in range(T)]

dp = [0] * 12 # n은 양수이며 11보다 작다.
dp[1] = 1
dp[2] = 2
dp[3] = 4 

for i in range(4,12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for n in ns:
    print(dp[n])
