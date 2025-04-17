def solution(array, n): 
    array.sort(key= lambda x: (abs(n-x), x-n))
    return array[0]
               