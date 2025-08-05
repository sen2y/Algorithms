import sys
input = sys.stdin.readline

AN, BN = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

cnt = 0
print(len(A-B) + len(B-A))