def solution(s): 
    total = []
    arr = s.split(' ')
    for i in arr:
        if len(total) > 0 and i == 'Z': total.pop()
        elif i != 'Z':
            total.append(int(i)) 
    if not total: return 0
    return sum(total) 