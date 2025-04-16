def solution(numbers): 
    sorted_array = sorted(numbers) 
    plus_max = sorted_array[-1] * sorted_array[-2]
    minus_max = sorted_array[0] * sorted_array[1]
    return max(plus_max, minus_max)