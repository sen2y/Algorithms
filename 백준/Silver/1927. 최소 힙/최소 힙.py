# 입력
import sys
import heapq

input = sys.stdin.readline
# 연산의 개수
N = int(input())

# 최소힙 배열
heap = []
for _ in range(N):
    x = int(input())
    # 만약 x가 자연수라면 x추가, 0이라면 가장 작은값 출력하고 배열에서 제거
    if x==0:
        if len(heap)==0: print(0)
        else: print(heapq.heappop(heap))
    else: heapq.heappush(heap, x)
# 최소힙 
# 자연수 x를 배열에 넣어 가장 작은값 출력하고 그 값을 배열에서 제거한다.
# 입력에서 0이 주어진 횟수만큼 답을 출력한다.
# 배열이 비어있는데 가장 작은 값 출력해야하는 경우 0을 출력한다.