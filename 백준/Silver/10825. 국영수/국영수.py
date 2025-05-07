import sys
input = sys.stdin.read

data = input().strip().split('\n')
n, data = int(data[0]), data[1:]

# 국어, 영어, 수학 점수가 공백으로 주어진다. 
# 정렬 기준
# - 국어점수 내림차순
# - 국어점수 같으면 영어점수 오름차순
# - 국영 같으면 수학 낼미차순
# - 모두같으면 이름 사전 순 대문자가 더 앞으로

info = []
for i in data:
    name, k, e, m = i.split()
    info.append([name, int(k), int(e), int(m)]) 

info.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
print('\n'.join([i[0] for i in info]))

