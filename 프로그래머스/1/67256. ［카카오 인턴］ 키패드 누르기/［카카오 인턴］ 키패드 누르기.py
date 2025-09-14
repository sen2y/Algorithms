# 12
def solution(numbers, hand):
    graph = {1: (0,0), 2:(1, 0), 3:(2, 0), 4:(0,1), 5: (1,1), 6:(2,1), 7:(0,2), 8:(1,2), 9:(2,2), 0:(1,3)}
    answer = ''
    hand = "L" if hand == 'left' else 'R'
    pl, pr = (0,3), (2,3)
    for n in numbers:
        if n in [1,4,7]: 
            print(n, 'L')
            answer += 'L'
            pl = graph[n]
        elif n in [3,6,9]: 
            print(n, 'R')
            answer += 'R'
            pr = graph[n]
        # 가운데 열 2,5,8,0: 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
        else: 
            disl = abs(pl[0] - graph[n][0]) + abs(pl[1] - graph[n][1])
            disr = abs(pr[0] - graph[n][0]) + abs(pr[1] - graph[n][1])
            print(disl, disr)
            if disl < disr: 
                answer += 'L'
                pl = graph[n]
            elif disl == disr: 
                answer += hand 
                if hand == "L": pl = graph[n]
                else: pr = graph[n] 
            else: 
                answer += 'R'
                pr = graph[n]
            
    
    return answer