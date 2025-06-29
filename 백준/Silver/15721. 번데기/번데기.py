# 게임인원 a, 구하고자하는 번째 t, 구호 0(뻔) 1(데기)
# n회차때 나오는 단어의 수 4+2(n+1)
from itertools import cycle
from itertools import cycle

a = int(input())
t = int(input())
flag = int(input())

def solution(a, t, f):  
    turns = cycle(range(a))
    count = 0
    n = 1
    while True: 
        # 기본 4턴
        for word in [0, 1, 0, 1]:
            person = next(turns)
            if word == f:
                count += 1
                if count == t:
                    print(person)
                    return
        # 추가 반복: 뻔 n+1번
        for _ in range(n+1):
            person = next(turns)
            if f == 0:
                count += 1
                if count == t:
                    print(person)
                    return
        # 추가 반복: 데기 n+1번
        for _ in range(n+1):
            person = next(turns)
            if f == 1:
                count += 1
                if count == t:
                    print(person)
                    return
        n += 1
             
solution(a, t, flag)