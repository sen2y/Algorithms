# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 
import sys
input = sys.stdin.readline
N = int(input().strip())

costs = [list(map(int, input().split())) for _ in range(N)]
# print(costs)

# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다. 
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
dp = [[0] * 3 for _ in range(N)]
# print(dp)

dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

for i in range(1, N):
    for j in range(3):
        if j==0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + costs[i][j]
        elif j==1:
            # print(i, dp[i-1][0], dp[i-1][2], costs[i][j])
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + costs[i][j]
            # print(dp[i][j])
        else:
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + costs[i][j]
# print(dp)
# print(sorted(dp[N-1])[0])
print(min(dp[N-1]))




# 첫째 줄에 모든 집을 칠하는 비용의 최솟값