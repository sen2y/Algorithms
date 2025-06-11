import sys
input = sys.stdin.read

arr = []
lines = list(input().rstrip().split('\n'))
for line in lines:
    nums = map(int, line.split())
    arr.extend(nums)
 
result = []
for i in arr[1:]:
    reversed_num = int(str(i)[::-1])  
    result.append(reversed_num)

result.sort()
print('\n'.join(map(str, result)))