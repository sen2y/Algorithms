def solution(order):
    count=0
    for i in str(order):
        if i!='0' and int(i)%3==0: count+=1 
    return count
 