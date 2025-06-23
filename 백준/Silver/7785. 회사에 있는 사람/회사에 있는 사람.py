import sys
input = sys.stdin.readline

N = int(input())
result = {}
for _ in range(N):
    name, log = input().split()
    if log == 'enter': result[name] = 1
    else: 
        if name in result: del result[name]

for name in sorted(result.keys(), reverse=True): print(name)