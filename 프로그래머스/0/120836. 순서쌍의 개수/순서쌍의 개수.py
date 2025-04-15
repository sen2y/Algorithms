def solution(n):
    count = 0
    for i in range(n):
        if n % (i+1) == 0: count+=1
    return count