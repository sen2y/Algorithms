def solution(n):
    total = 1
    for i in range(10):
        total *= i+1 
        if total > n: return i
    return 10