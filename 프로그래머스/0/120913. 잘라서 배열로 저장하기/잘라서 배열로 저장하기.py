def solution(my_str, n): 
    answer = []
    cnt = 0;  
    while cnt < len(my_str) / n:
        answer.append(my_str[cnt*n:(cnt+1)*n])
        cnt+=1
    return answer