import sys

input = sys.stdin.readline
n = int(input())
words = [input().strip() for _ in range(n)]

def check(word):
    answer = ''
    mapping = {}
    count = 0
    for st in word:
        if st not in mapping:
            mapping[st] = count
            count+=1
        answer += str(mapping[st])
    return answer

 

result = 0
for i in range(n):
    for j in range(n-i-1): 
        if check(words[i]) == check(words[j+1+i]):
            result+=1

print(result)


