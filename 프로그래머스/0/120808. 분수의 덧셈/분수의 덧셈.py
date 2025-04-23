from math import gcd

def lcm(a,b): # 최소공배수
    # 두수의 곱을 두수의 최소공약수로 나눈 값
    return a*b // gcd(a,b) 

def solution(numer1, denom1, numer2, denom2):
    l = lcm(denom1, denom2)
    print(l)
    x1, x2 = l // denom1, l // denom2
    print(x1, x2) 
    g = gcd(numer1*x1 + numer2*x2,l) 
    return [(numer1*x1 + numer2*x2)//g, l//g]
 