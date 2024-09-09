def solution(nums):  
    len_num = len(nums) / 2
    dict = {}
    for v in nums:
        if v in dict: 
            dict[v] += 1
        else:
            dict[v] = 1
    max_num = 0
    for v in dict:  
        if dict[v] > 0 :
            max_num += 1
    if max_num > len_num : return len_num
        
    return max_num
 