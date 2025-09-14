#45
def solution(survey, choices):
    dict = {}
    for i in range(len(survey)):
        s, choice = survey[i], choices[i]
        n, y = s[0], s[1] 
        if choice>3: 
            dict[n] = dict.get(n, 0) + (4-choice)
        else:   
            dict[y] = dict.get(y, 0) + (choice-4)
    result = []
    # 1번
    if dict.get('R', 0) >= dict.get('T',0): result.append('R')
    else: result.append('T')
    # 2번
    if dict.get('C', 0) >= dict.get('F',0): result.append('C')
    else: result.append('F')
    # 3번
    if dict.get('J', 0) >= dict.get('M',0): result.append('J')
    else: result.append('M')
    # 4번
    if dict.get('A', 0) >= dict.get('N',0): result.append('A')
    else: result.append('N')
    

        
    # 각 성격유형 차례로 점수가 높은 유형 출력
    # 동일한 점수이면 사전순
    
    
    
    print(''.join(result))
    return ''.join(result)
