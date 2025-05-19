import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []
cur = 1
is_possible = True

for _ in range(N):
    x = int(input())
    while cur <= x:
        stack.append(cur)
        result.append('+')
        cur += 1
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        is_possible = False
        break

if is_possible:
    print('\n'.join(result))
else:
    print("NO")