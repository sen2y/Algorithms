import sys
input = sys.stdin.readline

# 첫째 줄에 수의 개수, 홀수 N(1 ≤ N ≤ 500,000)
# 그 다음 N개의 줄에는 정수들 절댓값은 4,000을 넘지 않는다.
N = int(input())
nums = []
nums_cnt = {}
for _ in range(N):
    num = int(input())
    nums.append(num)
    nums_cnt[num] = nums_cnt.get(num, 0) + 1

# 출력
nums.sort()
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림
print(int(round(sum(nums)/N, 0)))
# 둘째 줄에는 중앙값을 출력한다.
print(nums[N//2])
# 셋째 줄에는 최빈값을 출력한다. 여러개면 두번째로 작은 값
max_cnt = max(nums_cnt.values())
max_nums = [num for num, cnt in nums_cnt.items() if cnt == max_cnt]
max_nums.sort()
if len(max_nums) > 1: print(max_nums[1])
else: print(max_nums[0])
# 넷째 줄에는 범위를 출력한다.
print(nums[-1]-nums[0])