def solution(today, terms, privacies):
    ty, tm, td = map(int, today.split('.'))
    tdays= ty*12*28 + tm*28 + td
    # print(ty, tm, td)
    # 모든 달은 28일까지 있다고 가정
    tlist = {arr.split(' ')[0]: arr.split(' ')[1] for arr in terms}
    plist = [arr.split() for arr in privacies]

    answer = []
    for i, (p, kind) in enumerate(plist, 1):
        time = int(tlist[kind]) 
        py, pm, pd = map(int, p.split('.'))
        pdays = py*12*28 + pm*28 + pd
        print(tdays, pdays + time*28 - 1)
        if tdays > pdays + time*28 - 1: answer.append(i)
        
    return answer