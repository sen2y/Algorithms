import sys
input = sys.stdin.readline

N = int(input())
ns = sorted(map(int, input().split()))

low, high = 0, N-1
res = float('inf')
ans = (0,0)

while low<high:
    sum = ns[low] + ns[high]
    if abs(sum) < res: 
        res = abs(sum)
        ans = (ns[low], ns[high]) 
    if sum>=0:
        if sum==0: 
            break 
        high -= 1
    else: low += 1

print(' '.join(map(str,ans)))
