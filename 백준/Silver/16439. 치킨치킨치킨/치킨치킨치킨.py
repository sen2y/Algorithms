import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
prefs = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0

for c1, c2, c3 in combinations(range(M), 3):
    total = 0
    for i in range(N):
        best = max(prefs[i][c1], prefs[i][c2], prefs[i][c3])
        total += best
    if total > max_sum: max_sum = total

print(max_sum)