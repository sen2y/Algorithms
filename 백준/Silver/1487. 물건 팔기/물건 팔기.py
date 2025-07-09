import sys
input = sys.stdin.readline

N = int(input())

list = []
for _ in range(N):
    a, b = map(int,input().split())
    list.append((a,b))
list.sort()

max_benefit = 0
result = 0

for price, minus in list:
    benefit = 0
    for x2, y2 in list:
        if x2 >= price and y2 < price: 
            benefit += price-y2
    if max_benefit < benefit:
        max_benefit = benefit
        result = price
    # max_benefit = max(max_benefit, benefit)

print(result)




