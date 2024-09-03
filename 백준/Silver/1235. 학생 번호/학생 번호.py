n = int(input())  
arr = [input().strip() for _ in range(n)]   

str_len = len(arr[0])

for i in range(1, str_len + 1):
    answers = set()
    for j in range(n):
        answers.add(arr[j][-i:])  
    if len(answers) == n:  
        print(i) 
        break