def solution():
    n, x = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    addlist = [];
    
    for i in range(n):
        if (i==0): 
            addlist.append(arr[i])
        else: 
            addlist.append(arr[i] + addlist[i-1]) 

    max_sum = addlist[x - 1]
    cnt = 1;

    for i in range(x, n):  
            num = addlist[i] - addlist[i-x]
            if (max_sum < num) : 
                max_sum = num
                cnt = 1;
            elif (max_sum == num) : 
                cnt += 1; 
    if (max_sum == 0) : 
        print('SAD')
    else:
        print(max_sum)
        print(cnt)
    
    

solution();