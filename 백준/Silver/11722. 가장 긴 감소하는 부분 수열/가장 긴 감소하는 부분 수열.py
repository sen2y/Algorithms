import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
# 부분 수열이란?
# 원래 수열에서 순서를 유지하면서 몇 개를 골라낸 수열

dp = [1] * N
for i in range(N): 
    for j in range(i):
        if A[j] > A[i]: dp[i] = max(dp[i], dp[j]+1)
   

print(max(dp))