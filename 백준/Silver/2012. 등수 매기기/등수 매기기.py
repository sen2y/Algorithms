# 입력
# 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 500,000)
# 둘째 줄부터 N개의 줄에 걸쳐 각 사람의 예상 등수가 순서대로,  500,000 이하의 자연수
import sys
input = sys.stdin.readline

N = int(input())
ranks = []
for _ in range(N):
    ranks.append(int(input()))

# 출력
# 첫째 줄에 불만도의 합을 최소로 할 때, 그 불만도를 출력한다.
ranks.sort()
# print(ranks)
cur = 1
sum = 0
for rank in ranks:
    sum += abs(cur - rank)
    cur += 1
print(sum)
