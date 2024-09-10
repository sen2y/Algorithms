def solution(participant, completion):
    dict = {}
    for v in completion: 
        if v in dict : 
            dict[v]+=1;
        else : dict[v] = 1 
        
       # participant의 이름들을 확인
    for p in participant:
        # completion에 있는 이름일 경우
        if p in dict:
            if dict[p] > 1:
                dict[p] -= 1
            else:
                del dict[p]  # 1명만 있을 경우 딕셔너리에서 삭제
        else:
            # 딕셔너리에 없으면 이 사람이 완주하지 못한 사람
            return p
    for i in range(len(completion)):
        if dict[participant[i]] > 0:return participant[i] 