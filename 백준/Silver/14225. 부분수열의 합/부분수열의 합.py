import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())
S = list(map(int, input().split()))

possible_sum = set()

for i in range(1,N+1):
    for comb in combinations(S, i):
        possible_sum.add(sum(comb))

i = 1
while True:
    if i not in possible_sum:
        print(i)
        break;
    i+=1