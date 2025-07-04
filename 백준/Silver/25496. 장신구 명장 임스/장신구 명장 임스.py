import sys
input = sys.stdin.readline

P, N = map(int, input().split())
line = list(map(int, input().split()))

line.sort()
# print(line)
cnt = 0
for i in line:
    # print(P+i)
    if P < 200: 
        P += i
        cnt += 1
    else: break

print(cnt)