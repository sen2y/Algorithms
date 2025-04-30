import sys
input = sys.stdin.read

data = input().rstrip().split('\n')
n = int(data[0])
data = data[1:]

def solution(data):
    arr = [(*map(int,data[i].split()), i) for i in range(n)]
    result = [0]*n  
    
    for i in range(n): 
        rank = 1
        for j in range(n):
            if i == j: continue 
            if arr[j][0] > arr[i][0] and arr[j][1]>arr[i][1]: 
                rank+=1
        result[arr[i][2]] = rank 
    print(' '.join(map(str, result)))
        


solution(data)