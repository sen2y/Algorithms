def solution(polynomial):
    arr = polynomial.split()
    print(arr)
    # 홀수번째 인덱스는 무조건 + 부호
    a = 0 # x있는 수
    b = 0 # 정수
    for i in range(0, len(arr), 2): #부호는 제거
        if arr[i].isdigit(): b+=int(arr[i])
        else:
            if arr[i]=='x': a+=1
            else: a += int(arr[i][:-1])  
    if a == 0: return str(b)
    if b == 0: 
        if a==1: return 'x'
        return f"{a}x"
    if a==1: return f"x + {b}"
    return f"{a}x + {b}"
