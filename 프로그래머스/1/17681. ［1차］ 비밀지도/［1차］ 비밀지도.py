
def solution(n, arr1, arr2):
    arr = []
    for i in range(n):
        x, y = arr1[i], arr2[i]
        # xstr, ystr = [], []
        xstr, ystr = '',''
        # print(x)
        while x > 0:
            # xstr.append(x % 2)
            xstr+=str(x%2)
            x = x//2
        while len(xstr) < n: 
            xstr+=str(x)
        xstr =  xstr[::-1] 
        while y > 0:
            # ystr.append(y % 2)
            ystr+=str(y%2)
            y = y//2
        # ystr.append(y)
        while len(ystr) < n: 
            ystr+=str(y)
        ystr = ystr[::-1]
        # if len(ystr) < n: ystr+='0'
        print(xstr, ystr)
        arr.append(str(int(xstr)+int(ystr)))
        # print(arr)
   
    answer = []
    for i in arr:
        strs = ''
        print(999,i)
        while len(i) < n: i = '0' + i
        
          
        for j in i:
            if int(j)>0: strs+='#'
            else: strs+=' '
        # print(strs)
        answer.append(strs)
    print(answer)
    return answer