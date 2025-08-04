import sys
input = sys.stdin.readline

N, M = map(int, input().split())
spw = {}
for _ in range(N):
    site, pw = input().split()
    spw[site] = pw

for _ in range(M):
    site = input().strip()
    print(spw[site]) 