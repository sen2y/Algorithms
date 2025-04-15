def solution(rsp): 
    arr = ["2","0","5"] 
    
    return ''.join([arr[(arr.index(i)+1)%3] for i in rsp])