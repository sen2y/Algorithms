import sys
input = sys.stdin.read

data = input().rstrip().split('\n')
n, m = int(data[0]), int(data[1]) 
data = data[2].split() 
data = [int(i) for i in data if int(i) < m] ## m보다 큰 경우는 제외

def solution(n, m, data):
    # 오름차순 정렬을해 
    cnt = 0
    for i in data:
        if i!=m-i and (m-i) in data: cnt+=1
    
    print(cnt//2)



solution(n,m,data)