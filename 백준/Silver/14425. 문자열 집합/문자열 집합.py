import sys
input = sys.stdin.read

data = input().rstrip().split('\n')
# 첫째줄
n, m = map(int, data[0].split())
s = data[1:n+1]
test = data[n+1:]
# print(s, test)

cnt = 0
for i in test:
    if i in s: cnt+=1

print(cnt)