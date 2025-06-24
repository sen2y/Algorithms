# 문자 순: B < S < G < P < D
# 숫자 내림차순
def diff(key):
    level_order = {'B': 0, 'S': 1, 'G': 2, 'P': 3, 'D': 4}
    letter = key[0]
    number = int(key[1:])
    return (level_order[letter], -number)

import sys
input = sys.stdin.readline
N = int(input())
levels = input().split()

sorted_levels = sorted(levels, key=diff)

if levels == sorted_levels: print("OK")
else:
    result = sorted([levels[i] for i in range(N) if levels[i] != sorted_levels[i]], key=diff)
    print("KO")
    print(' '.join(result))


