def solution(before, after): 
    a = list(after)
    if after == before[::-1]: return 1
    for i in before:
        if i in a: a.remove(i)
    if len(a)==0: return 1
    return 0