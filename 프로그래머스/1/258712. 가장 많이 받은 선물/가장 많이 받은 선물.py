def solution(friends, gifts):
    n = len(friends)
    idx = {f: i for i,f in enumerate(friends)} # 이름별 인덱스 지정
    
    giftlist = [[0]*n for _ in friends] # 주고받은 선물기록
    givenum = [0]*n
    getnum = [0]*n
    
    result = [0]*n
    
    for gift in gifts:
        a, b = gift.split()
        print(a, b, idx[a], idx[b])
        giftlist[idx[a]][idx[b]] += 1
        print(giftlist[idx[a]][idx[b]])
        givenum[idx[a]] += 1
        getnum[idx[b]] += 1
    
    print(giftlist, givenum, getnum)
    
    for i in range(n):
        for j in range(i+1, n):
            print(i, j)
            # na, nb = idx[i], idx[j]
            if i == j: continue
            # a가 b보다 선물많이 준경우
            if giftlist[i][j] > giftlist[j][i]:
                # b가 a에게 선물준다.
                result[i] += 1
                print(111, i)
            elif giftlist[i][j] < giftlist[j][i]:
                # a가 b에게 선물준다.
                result[j] += 1
                print(2222, j)
            else: # 선물주고받은횟수 동일하다면
                # 선물지수가높은 사람이 선물받는다.
                if (givenum[i] - getnum[i]) >  (givenum[j] - getnum[j]):
                    result[i] += 1
                    print(giftlist[i][j] , giftlist[i][j])
                    print(3333, i)
                elif (givenum[i] - getnum[i]) <  (givenum[j] - getnum[j]):
                    result[j] += 1
                    print(444, j)
            
    # print(result)
    result.sort(reverse=True)
    return result[0]
                  