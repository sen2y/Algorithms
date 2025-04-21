import sys
input = sys.stdin.read
data = input().strip().split('\n')

def solution(data):
    a, b = data 
    cnt = 0
    i = 0 
    while i < len(a): 
        if a[i:i+len(b)] == b: 
            cnt += 1
            i+=len(b)
        else: i+=1 
    print(cnt) 


solution(data)
