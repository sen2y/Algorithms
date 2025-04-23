from math import gcd
def solution(a, b):
    # 최대공약수 찾아보자 gcd
    g = gcd(a,b) # g는 a,b의 최대공약수. 
    # a/b를 기약분수로 만들어 b가 2,5 로만 나뉘는지 확인
    # b만 필요하므로 b만 계산
    b //= g
    ## 2,5로만 나뉘면 1, 아니면 2 return
    for i in [2,5]: 
        while b%i==0:
            b//=i  
    return 1 if b==1 else 2