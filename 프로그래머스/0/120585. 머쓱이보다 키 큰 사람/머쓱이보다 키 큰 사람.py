def solution(array, height): 
    arr = [i for i in array if i > height]
    return len(arr)