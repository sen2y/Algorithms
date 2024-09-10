n = int(input())
answer = list(map(str, input().split(" ")))
inputs = list(map(str, input().split(" ")))

dict = {}
for i, v in enumerate(answer):
    dict[v] = i 

list = []
for i in inputs:
    list.append(dict[i]) 

# 총 가능한 순서쌍의 수
total = int(n * (n-1) / 2) 
cnt = 0

# n == 2일 때 두 개의 순서쌍을 비교
if n == 2:
    if list[0] < list[1]:
        cnt = 2  # 올바르게 정렬된 경우
    print(f"{cnt}/2")
else:
    # i < j를 만족하는 순서쌍을 찾기
    for i in range(n):
        for j in range(i + 1, n):
            if list[i] < list[j]: 
                cnt += 1
    
    print(f"{cnt}/{total}")
