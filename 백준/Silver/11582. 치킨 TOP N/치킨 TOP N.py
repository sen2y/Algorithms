import sys
input = sys.stdin.readline

N = int(input()) # N은 항상 2의 거듭제곱 꼴이다.
scores = list(map(int, input().split()))
k = int(input()) #  현재 정렬을 진행중인 회원들의 수, 2의 거듭제곱

result = []
for i in range(k):
    num = N//k 
    result.extend(sorted(scores[i*(num):(i+1)*(num)]))

print(' '.join(map(str, result)))