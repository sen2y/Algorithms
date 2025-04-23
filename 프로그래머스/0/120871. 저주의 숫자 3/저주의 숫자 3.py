def solution(n):
    cnt = 1 # 1부터 n개까지 n개 세면 끝
    i = 1 # 실제 그마을에서의 숫자  (1,2,4,,,)
    while cnt <= n:
        # print('i:', i, 'cnt:',cnt,'n:', n)
        # 3의 배수이거나, 3이 들어간 수는 cnt++
        if (i%3 == 0 or '3' in str(i)): 
            print('a')
        # 그마을에서 사용하는 수면 cnt 증가
        else: cnt+=1  
        # print('b')
        i+=1
    return i-1