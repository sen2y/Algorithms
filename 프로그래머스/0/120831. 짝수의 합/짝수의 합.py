def solution(n): 
    # answer = [i for i in range(2, n + 1, 2)] # 컴프리헨션 코드로 줄일 수 있다
    # print(answer) # 	[2, 4, 6, 8, 10]
    return sum([i for i in range(2, n + 1, 2)])
    # sum = 0
    # for i in range(n+1):
    #     if (i%2 == 0):
    #         sum+=i
    # return sum