def solution(arr, idx):
    if 1 in arr[idx:] :   
        return arr.index(1, idx)
    else :
        return -1
  