import sys
input = sys.stdin.read
data = list(map(int,input().rstrip().split('\n')))

n = int(data[0])
data = data[1:]

def solution(data):
    data.sort(reverse=True)
    sum = 0
    for idx,i in enumerate(data):
        sum+= i-(idx) if i-idx>0 else 0 
    print(sum)

solution(data)