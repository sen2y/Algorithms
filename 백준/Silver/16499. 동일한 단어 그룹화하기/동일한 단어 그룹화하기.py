import sys
input = sys.stdin.readline

N = int(input())
words = [list(input().strip()) for _ in range(N)]

result = []
for word in words:
    word.sort()
    result.append(''.join(word)) 

print(len(set(result)))

 
 