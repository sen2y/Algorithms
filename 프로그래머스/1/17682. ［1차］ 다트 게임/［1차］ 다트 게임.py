def solution(dartResult):
    # Single(S), Double(D), Triple(T) 영역 
    # 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산
    
    # 스타상(*)은 해당 점수와 바로 전에 얻은 점수를 각 2배,
    # 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배
    # 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다.
    
    # 아차상(#) 당첨 시 해당 점수는 마이너스된다.
    # 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
    answer = 0
    nums = []
    # dartResult = dartResult.replace('S', '')
    for idx, k in enumerate(dartResult): 
        if k.isdigit(): 
            if dartResult[idx-1].isdigit(): nums[-1] = 10
            else: nums.append(int(k))
        elif k == 'D': 
            nums[-1] = nums[-1]**2
        elif k == 'T':
            nums[-1] = nums[-1]**3
        elif k == '*': 
            if len(nums) > 1:
                nums[-1], nums[-2] = nums[-1]*2, nums[-2]*2
            else:
                nums[-1] = nums[-1]*2
        elif k == '#':
            nums[-1] = nums[-1]*(-1)

    print(nums)
    return sum(nums)