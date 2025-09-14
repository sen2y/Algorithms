def solution(N, stages):
    # 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
    stages.sort()
    rate = {}
    total, cnt = 0, 0
    for i in range(1, N+1):
        total += cnt
        cnt = 0
        for j in stages[total:]:
            if j > i: break;
            cnt += 1
            #  아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
        
        rate[i] = 0 if cnt==0 else cnt/(len(stages)-total) 
        # print(rate)
    # 실패율이 높은 스테이지부터 내림차순으로
    # 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
    # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
    rate = sorted(rate, key=lambda x: (-rate[x], x))
    # print(rate) 
    return rate