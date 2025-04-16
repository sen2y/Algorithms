def solution(my_string):  
    # count = 0
    # temp = ''
    # for idx, i in enumerate(my_string): 
    #     if i.isdigit():
    #         temp+=i
    #         if idx == len(my_string)-1:  
    #             count+=int(temp)
    #     else:
    #         if temp!='':  
    #             count+=int(temp)
    #         temp='' 
    # return count
    return sum(map(int,''.join(i if i.isdigit() else ' ' for i in my_string).split()))
 