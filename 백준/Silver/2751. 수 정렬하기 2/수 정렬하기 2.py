import sys
input = sys.stdin.readline
N = int(input())


arr = [int(input().strip()) for _ in range(N)]
print('\n'.join(map(str, sorted(arr))))
