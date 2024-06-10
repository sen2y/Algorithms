def solution(arr, intervals):
    a, b = intervals[0]
    c, d = intervals[1]
    return arr[a:b+1] + arr[c:d+1]
    # return answer