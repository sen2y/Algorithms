import sys
input = sys.stdin.read
 
data = input().strip().split('\n')
n, m = data[0].split()
n, m = int(n), int(m) 
a = [] # 듣도
b = [] # 보도
for i in range(1, 1+n): # 듣도 사람 리스트
    a.append(data[i])
for j in range(n+1,n+m+1):
    b.append(data[j])  
c = set(a) & set(b)
print(len(c))
print('\n'.join(sorted(list(c))))


