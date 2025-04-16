def solution(my_string):  
    count = 0
    temp = ''
    for idx, i in enumerate(my_string):
        print(0, i)
        if i.isdigit():
            temp+=i
            if idx == len(my_string)-1: 
                print(222, i, temp)
                count+=int(temp)
        else:
            if temp!='': 
                print(1, temp)
                count+=int(temp)
            temp=''
    print(2, count)
    return count

solution('12aaa33aa2')