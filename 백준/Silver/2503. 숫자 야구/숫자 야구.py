import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
q = []
for _ in range(N):
    num, st, ba = input().split()
    q.append((num, int(st), int(ba)))
    # print(x, s, b)

# 중복없이 가능한 경우
all = permutations('123456789',3)

answer = 0

for i in all:
    i_str = ''.join(i)
    is_valid = True
    # print(1)

    for qnum, qst, qba in q:
        strike = 0
        ball = 0
        # print(qnum)
        for j in range(3):
            if i_str[j] == qnum[j]: strike += 1
            elif i_str[j] in qnum: ball += 1
        if strike != qst or ball != qba:
            is_valid = False
            # print('break')
            break

    if is_valid: answer += 1
print(answer)




    




