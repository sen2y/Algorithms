def solution(array, n): 
    array.append(n)
    a = sorted(array)
    idx = a.index(n)
    if idx == len(a) - 1: return a[idx-1] 
    if idx == 0: return a[idx+1]
    return a[idx-1] if n-a[idx-1] <= a[idx+1]-n else a[idx+1]

