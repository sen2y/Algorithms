import sys
# 동명이인은 없으며, 사람의 이름은 대소문자를 구분한다. 
input = sys.stdin.readline
N = int(input())
names = {'ChongChong': 1}
for _ in range(N):
    a, b = input().split()  
    if names.get(a, 0) == 1 or names.get(b,0) == 1:   
        names[a] = 1
        names[b] = 1

print(sum(names.values()))