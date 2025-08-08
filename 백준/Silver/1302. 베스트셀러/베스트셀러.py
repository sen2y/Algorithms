import sys
input = sys.stdin.readline

N = int(input())
books = {}

for _ in range(N):
    name = input().strip()
    books[name] = books.get(name, 0) + 1

maxv = max(books.values())
maxn = [i for i,j in books.items() if j == maxv]
print(sorted(maxn)[0])