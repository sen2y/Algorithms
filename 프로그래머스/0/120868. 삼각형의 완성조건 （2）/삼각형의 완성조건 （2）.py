def solution(sides):
    fir, sec = sorted(sides)
    print(fir, sec)
    cnt = 0 
    # sec이 가장 긴 변일떄
    # fir + new > sec 이어야함
    # new > sec - fir
    # sec - fir < new < sec
    for i in range(sec-fir, sec): cnt+=1
    # new가 가장 긴 변일때
    # fir + sec > new > sec
    for j in range(sec, fir+sec): cnt+=1
    return cnt-1
        
            