import sys
input = sys.stdin.read
 
data = input().rstrip().split('\n')
n = data[0]

data = data[1:]
print('\n'.join(sorted(set(data), key=lambda x: (len(x), x))))