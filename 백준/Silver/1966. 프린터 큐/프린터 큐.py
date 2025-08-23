import sys
from collections import deque
input = sys.stdin.readline

TN = int(input())

for _ in range(TN):
    # 문서의 개수 N, 
    # 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지 M
    N, M = map(int, input().split())
    # deque에는 sort가 없다.
    arr = list(map(int, input().split()))
    q = deque((p, i) for i, p in enumerate(arr)) 

    cnt = 1
    while True:
        p, i = q[0]  
        if p < max(q, key = lambda x: x[0])[0]:
            q.append(q.popleft())

        else:
            q.popleft()
            if M == i: 
                print(cnt)
                break;
            cnt += 1
        


