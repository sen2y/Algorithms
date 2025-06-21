import sys
input = sys.stdin.readline

# 멜로디에 포함되어 있는 음의 수 N, 한 줄에 있는 프렛의 수 P
N, P = map(int, input().split()) 
stack = [[] for _ in range(7)]
cnt = 0

for _ in range(N):
    line, fret = map(int, input().split()) 
    while stack[line] and stack[line][-1] > fret: 
        stack[line].pop()
        cnt += 1
    
    if not stack[line] or stack[line][-1] != fret: 
        stack[line].append(fret)
        cnt += 1

print(cnt)
    