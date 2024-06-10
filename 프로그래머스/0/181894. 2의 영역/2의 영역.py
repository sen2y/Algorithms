def solution(arr):
    list = [idx for idx, ele in enumerate(arr) if ele == 2]
    if len(list) == 0:
        return [-1]
    elif len(list) == 1:
        return [2]
    return arr[list[0]:list[-1]+1]