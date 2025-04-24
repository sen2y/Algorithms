import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

data = input().rstrip().split('\n')
n, m, r = map(int, data[0].split())
data = data[1:]
cnt = 1

def solution(data):
    global cnt
    # 인접리스트 생성
    graph = [[] for _ in range(n+1)]
    for i in data:
        u, v = map(int,i.split())
        graph[u].append(v)
        graph[v].append(u) 
    # 오름차순 정렬 ( 번호 작은 순으로 방문하도록 정렬 )
    for i in graph:
        i.sort() 

    # 방문 순서 기록용 배열
    visited = [0]*(n+1)  
     
    # dfs 정의
    def dfs(node):
        global cnt 
        visited[node]=cnt
        cnt+=1
        for i in graph[node]:
            if visited[i]==0: 
                dfs(i)

    # dfs 실행 시작노드r
    dfs(r)

    # 결과 출력
    for i in range(1, n+1):
        print(visited[i])

solution(data)