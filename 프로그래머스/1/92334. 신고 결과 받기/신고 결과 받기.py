def solution(id_list, report, k):
    # 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다 
    # k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
    # 메일을 보내기 위해 신고당한 유저: [신고자1,신고자2] 딕셔너리 만들고
    # 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리 : set 집합으로 관리 
    
    
    record = {name:set() for name in id_list}
    for names in report:
        a, b = names.split()
        record[b].add(a)
        # print(record[b])

    
    # 신고한 유저: cnt 딕셔너리도 하나만든다
    cntdic = {name: 0 for name in id_list}
    
    topcnt = [values for name, values in record.items() if len(values) >= k]
    # print(topcnt)
    for names in topcnt:
        for name in names:
            cntdic[name] = cntdic.get(name, 0) + 1
    result = [num for name, num in cntdic.items()]
    # print(topcnt, cntdic, result)
    
    
    
    # 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 
    return result