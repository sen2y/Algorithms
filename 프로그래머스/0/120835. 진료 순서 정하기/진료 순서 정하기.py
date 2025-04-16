def solution(emergency): 
    st_arr = sorted(emergency, reverse=True) 
    return [st_arr.index(i)+1 for i in emergency]