def solution(s): 
    st = sorted(list(s)) 
    answer = []
    remove = ''
    print(st)
    for idx, i in enumerate(st):  
        if idx==0: answer.append(i)  
        elif (len(answer)>0) and (i == answer[-1]): 
            remove = answer.pop() 
        elif i != remove:  
            answer.append(i) 
    return ''.join(answer)