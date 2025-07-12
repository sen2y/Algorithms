import sys
import math
from collections import Counter

input = sys.stdin.readline

N = int(input().strip())
points = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(N):
    x0, y0 = points[i]

    dirs = Counter()
    for j in range(N):
        if i == j: continue
        dx = points[j][0] - x0
        dy = points[j][1] - y0
        g = math.gcd(dx, dy)
        dx //= g
        dy //= g
        dirs[(dx, dy)] += 1

    ordered_pairs = 0
    for (dx, dy), cnt in dirs.items():
        perp1 = (-dy, dx)
        perp2 = (dy, -dx)
        ordered_pairs += cnt * (dirs[perp1]+dirs[perp2])


    answer += ordered_pairs //2
print(answer)



