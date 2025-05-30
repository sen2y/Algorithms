# 첫째 줄에는 고속도로에 있는 충전소의 수 n > 0 양의 정수
# 둘째 줄부터 n개 줄에는 충전소의 위치 (위치는 더슨 크릭과 떨어진 거리) 0보다 크거나 같고, 1422보다 작거나 같다.
# 입력의 마지막 줄에는 0이 주어진다.

# 더슨 크릭 -> 델타 정션 -> 더슨 크릭 (2844마일)
# 완충시 한번에 200마일 이동 가능
# 충전소는 더슨크릭에 있고, 고속도로 중간중간에 있다.

import sys
input = sys.stdin.readline

n = int(input())
while n!=0:
    is_p = True
    # print('while 다시 시작')
    loc = []
    for _ in range(n): loc.append(int(input()))
    loc.sort()
    # print(loc)
    for i in range(n-1):
        if (loc[0] > 200) or (1422 - loc[-1] > 100) or (loc[i+1] - loc[i] > 200): 
            print('IMPOSSIBLE')
            is_p = False
            break              
    if is_p == True: print('POSSIBLE')
            
    n = int(input())


