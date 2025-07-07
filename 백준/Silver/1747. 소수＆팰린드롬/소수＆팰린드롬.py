import sys
input = sys.stdin.readline

N = int(input())

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0: return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

while True:
    if is_prime(N) and is_palindrome(N):
        print(N)
        break
    N+=1