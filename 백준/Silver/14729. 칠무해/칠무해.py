import sys
import heapq

input = sys.stdin.readline
N = int(input())
    
heap = [] # 최대힙
for i in range(N):
    score = float(input())
    if len(heap) < 7: heapq.heappush(heap, -score)
    else:
        if -score > heap[0]: heapq.heappushpop(heap, -score)
result = sorted([-x for x in heap])
for j in result:
    print(f"{j:.3f}")