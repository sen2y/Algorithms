import sys
input = sys.stdin.readline

word = input().rstrip()
result = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)): 
        first = word[:i][::-1]
        second = word[i:j][::-1]
        last = word[j:][::-1]
        result.append(first+second+last)
result.sort()
print(result[0])