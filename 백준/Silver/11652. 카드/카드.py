import sys
input = sys.stdin.readline

N = int(input())
nums = {}
for _ in range(N):
    num = int(input())
    if num in nums: nums[num]+=1
    else: nums[num] = 1
# 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
sort_num = sorted(nums.items(), key=lambda x: (-x[1], x[0]))

print(sort_num[0][0])