import sys
input = sys.stdin.readline

X = int(input())
cnt = 0
for i in range(1, X+1):
    if i < 100:  cnt+=1
    else:
        arr = str(i)
        if int(arr[1]) - int(arr[0]) == int(arr[2]) - int(arr[1]): 
            cnt+=1
print(cnt)
        
