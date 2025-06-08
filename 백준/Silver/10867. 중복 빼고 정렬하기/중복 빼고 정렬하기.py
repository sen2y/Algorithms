import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
print(' '.join(map(str, sorted(set(arr))))) 