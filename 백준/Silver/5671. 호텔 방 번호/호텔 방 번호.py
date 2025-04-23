import sys
input = sys.stdin.read
data = input().rstrip().split('\n') 
def solution(data):
    # print(data,22)
    # 호텔 방 번호는 N보다 크거나 같고, M보다 작거나 같아야 한다
    for i in data:
        n, m = i.split()
        # print(n,m)
        cnt = 0
        for j in range(int(n), int(m)+1):
            if len(set(str(j))) == len(str(j)): cnt+=1
        print(cnt)
    
    # 호텔 방 번호는 N보다 크거나 같고, M보다 작거나 같아야 한다
    # return 

solution(data)
