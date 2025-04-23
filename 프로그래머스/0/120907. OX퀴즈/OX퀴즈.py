def solution(quiz):
    new_arr = []
    for i in quiz: 
        new_arr.append(i.split())
        # 0,2 번째 정수
        # 1번째 부호
        # 3번째 =
        # 4번째 답
    # 0 과 2를 1로 연산한 값이 4와 동일한지 확인
    for idx,j in enumerate(new_arr):
        a, b = int(j[0]), int(j[2])
        real = 0
        if j[1] == '+' : real = a+b
        else: real = a-b
        # 4와 동일한가? 
        new_arr[idx] = "O" if str(real) == j[4] else "X"
    
    return new_arr