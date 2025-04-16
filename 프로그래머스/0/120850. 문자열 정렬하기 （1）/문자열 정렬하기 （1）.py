def solution(my_string): 
    return sorted([int(i) for i in my_string if ord(i)<97])