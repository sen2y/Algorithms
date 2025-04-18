def solution(my_string):
    stack = []
    arr = my_string.split()
    cnt = int(arr[0])
    print(arr)
    for i in arr:
        print(i)
        if i == '+' or i == '-': 
            print(1)
            stack.append(i)
            continue
        else:
            print(2)
            if stack: 
                print(3)
                op = stack.pop()
                if op == '+': cnt += int(i)
                else: cnt -= int(i)
        print(11, cnt)   
    return cnt

 
        