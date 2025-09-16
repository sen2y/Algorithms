from collections import defaultdict
def solution(edges):
    answer = []
    startd, endd = defaultdict(int), defaultdict(int)
    nodes = set()
    
    for a, b in edges:
        startd[a] += 1
        endd[b] += 1
        nodes.add(a)
        nodes.add(b)
    # print(startd, endd)
    
    # 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다.
    gen_node= -1
    for v in nodes:
        if startd[v] >=2 and endd[v] == 0: 
            gen_node = v
            break
    # gen_node, 도넛모양, 막대모양, 8자모양
    answer = [gen_node, 0, 0, 0]
    for v in nodes:
        if v == gen_node: continue
        # 막대 (마지막 노드의 startd==0, endd==1)
        elif startd[v] == 0:
            answer[2] += 1
        # 8자모양 (중앙에 started==2, endd==2)
        elif startd[v] >= 2 and endd[v] >= 2:
            answer[3] += 1
    print(answer)
    answer[1] = startd[gen_node] - answer[2] - answer[3]
            
    
    
    # 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수 return
    return answer