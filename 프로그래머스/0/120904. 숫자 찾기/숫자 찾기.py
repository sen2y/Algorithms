def solution(num, k):
    arr = list(str(num)) 
    return arr.index(str(k))+1 if str(k) in arr else -1