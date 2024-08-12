def checkNum():
    answer = []
    N = int(input()) 
    A = set(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    
    for num in B:
        if num in A: 
            answer.append(1)
        else:
            answer.append(0)
    
    # 각 정수를 문자열로 변환한 후, 줄바꿈으로 연결하여 출력
    print("\n".join(map(str, answer)))

checkNum()
