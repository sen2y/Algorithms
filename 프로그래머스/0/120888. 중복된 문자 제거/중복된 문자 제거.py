def solution(my_string): 
    arr = set([])
    answer=[]
    for i in my_string:
        if i not in arr: 
            arr.add(i)
            answer.append(i)
    return ''.join(answer)
        
        