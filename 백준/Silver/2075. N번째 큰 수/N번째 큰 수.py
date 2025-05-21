# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,500)
# 다음 N개의 줄에는 각 줄마다 N개의 수: -10억보다 크거나 같고, 10억보다 작거나 같은 정수
import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

# 힙크기를 N으로 제한해보자 
for _ in range(N):
    line = list(map(int, input().split())) 
    for i in line: 
        # print(i)
        if len(heap) < N: heapq.heappush(heap, i)
        else: 
            if i > heap[0]: heapq.heappushpop(heap, i)
# 출력 
# 첫째 줄에 N번째 큰 수를 출력한다. - 최대힙
# print(heap)
print(heap[0])
