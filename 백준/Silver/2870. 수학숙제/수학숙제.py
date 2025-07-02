import sys 
input = sys.stdin.readline

N = int(input()) 
numbers = []
for i in range(N):
    line = input().rstrip()
    num = ''
    for word in line: 
        # print(word, num,111)
        if word.isdigit(): 
            # print(word)
            num += word
            # print(num,999)
        else: 
            if num != '':
                # print(num, 333)
                numbers.append(int(num))
                # print(numbers, 888)
                num = ''
    if num != '': numbers.append(int(num))


numbers.sort()
print('\n'.join(map(str,numbers)))


