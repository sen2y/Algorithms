import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = [] 
for _ in range(N):
    # 수정: 원래 값을 그대로 ㄹ받고, 힙에 튜플형태로 (abs(x), x)형태로 넣어서 하게 하자. 
    # x = abs(int(input()))
    x = int(input())
    # 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력
    if len(heap)==0 and x == 0: print(0)
    elif x!=0: heapq.heappush(heap, (abs(x), x))
    elif x == 0: 
        print(heapq.heappop(heap)[1])
 