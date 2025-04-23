def solution(array):
    dic = {}   
    for i in array:
        dic[i] = dic.get(i, 0) +1
    val = sorted(dic.values(), reverse=True)
    max = val[0]  
    print(len(dic))
    if len(dic)==1: return array[0]
    if val[1] == max: return -1 
    for i in dic:
        if dic[i] == max: 
            print(i)
            return i
     