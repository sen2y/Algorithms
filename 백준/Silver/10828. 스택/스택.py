# 입력 
import sys
input = sys.stdin.readline
# 명령의 수 N (1 ≤ N ≤ 10,000)
N = int(input())
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다
# 정수를 저장하는 스택
stack = []
for _ in range(N):
    line = input().split()
    order = line[0] 
    # push X: 정수 X를 스택에 넣는 연산이다.
    if order == 'push': stack.append(int(line[1]))
    # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 빈스택이면 -1출력
    elif order == 'pop': print(-1 if len(stack)==0 else stack.pop()) 
    # size: 스택에 들어있는 정수의 개수를 출력한다.
    elif order == 'size': print(len(stack))
    # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif order == 'empty': print(1 if len(stack)==0 else 0)
    # top: 스택의 가장 위에 있는 정수를 출력한다. 빈스택이면 -1출력
    elif order == 'top': print(-1 if len(stack)==0 else stack[-1]) 