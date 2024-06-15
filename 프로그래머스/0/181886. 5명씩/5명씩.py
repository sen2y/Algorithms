def solution(names):
    # 간단 풀이
    return names[::5]
    # 나의 풀이
    # num = len(names) // 5
    # newArr = []
    # for i in range(num):
    #     newArr.append(names[i*5]) 
    # if len(names) > num*5 :
    #     newArr.append(names[num*5])
    # print(newArr)
    # return newArr