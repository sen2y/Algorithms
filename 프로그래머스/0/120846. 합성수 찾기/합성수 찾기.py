def solution(n):
    total = 0
    for i in range(n):
        cnt=0
        for j in range(i+2): 
            if (i+1)%(j+1) == 0: cnt+=1
        if cnt>=3: total+=1
    return total
        