def solution(n):
    k = n 
    answer = []
    while k != 1: 
        # 2~n따지 나눠보면서, 나눌 수 있는지. 나눌 수 있을때마다 다시 n으로 나눠줘야해
        for i in range(2, k+1):
            # i로 나눠지면? n/i까지 또 돌려서 나눠봐  
            if k%i == 0 : 
                answer.append(i) 
                k //= i 
                break
                
    # 출력: 소인수분해로 나오는 요소만 겹치지 않게 배열로 출력  
    return sorted(list(set(answer)))
# 입력: 숫자
