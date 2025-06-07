# 첫째 줄에 온라인 저지 회원의 수 N
# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름 입력은 가입한 순서로 주어진다.
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    age, name = input().split()
    arr.append((int(age), name, i))
arr.sort(key=lambda x: (x[0], x[2])) 

# 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순
for age, name, _ in arr: print(age, name)
