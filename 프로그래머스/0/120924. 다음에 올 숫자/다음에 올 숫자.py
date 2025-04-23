def solution(common): 
    a, b, c = common[-3], common[-2], common[-1]
    if b-a == c-b : return 2*c-b
    return c*(c//b)