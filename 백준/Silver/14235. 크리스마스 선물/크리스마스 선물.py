# 자신이 들고있는 가장 가치가 큰 선물 하나를 선물 - 최대힙
import sys
import heapq

# 첫 번째 줄에서는 아이들과 거점지를 방문한 횟수 n (1≤n≤5,000)
n = int(input())
heap = []
for _ in range(n):
    line = input().split()
    a = int(line[0])
    # a가 0일 때마다, 아이들에게 준 선물의 가치를 출력
    if a == 0: print(-heapq.heappop(heap) if len(heap)>0 else -1)
    # 다음 n줄에는 a가 들어오고, 그 다음 a개의 숫자가 들어온다.
    else:
        for i in range(a):
            heapq.heappush(heap, -int(line[i+1]))


