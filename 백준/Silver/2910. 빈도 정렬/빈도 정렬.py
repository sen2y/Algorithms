import sys
input = sys.stdin.readline

N, C = list(map(int, input().split()))
message = list(map(int,input().split()))

freq = {}
order = {}

for idx, n in enumerate(message):
    if n not in freq:
        freq[n] =1
        order[n] = idx
    else: freq[n] +=1
# (-빈도, 등장순) 기준으로 정렬
sorted_nums = sorted(freq.keys(), key=lambda x: (-freq[x], order[x]))

for num in sorted_nums:
    print((str(num) + ' ') * freq[num], end='')


