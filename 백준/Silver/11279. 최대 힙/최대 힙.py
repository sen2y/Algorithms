# 입력
import sys
import heapq
input = sys.stdin.readline

# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)
N = int(input())
heap = []
for _ in range(N):
    # 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x
    x = int(input())
    # 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산
    if x!= 0: heapq.heappush(heap, -x)
    
    else:
        # 출력
        # 입력에서 0이 주어진 횟수만큼 답을 출력
        # 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력
        if len(heap)==0: print(0)
        # x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거
        else: print(-heapq.heappop(heap))



