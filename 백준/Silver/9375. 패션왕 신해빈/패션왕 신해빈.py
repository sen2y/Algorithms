# 입력 : 
# 첫째줄 - 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)
# 이후, 해빈이가 가진 의상의 이름과 의상의 종류
import sys
# data = sys.stdin.readlines() #['2\n', '3\n', 'hat headgear\n', ... ]
data = [line.strip() for line in sys.stdin.readlines()] # .strip() 개행문자 제거
# print(data)

# input = sys.stdin.read
# data = input().strip().split('\n') # ['2', '3', 'hat headgear', 'sunglasses eyewear'..] 
# 로직 : 어떤 알고리즘으로 작업을 해줌
def solution(data):
    # answer
    n = int(data[0])
    idx = 1
    for _ in range(n):
        m = int(data[idx])# 각 케이스별 의상 수
        dic = {} # {key,val} 형태
        idx+=1
        for _ in range(m):
            # print(data[idx].split(' '), idx, m)
            name, category = data[idx].split(' ')
            # 딕셔너리 get(): category값이 없으면 0반환
            dic[category] = dic.get(category, 0) + 1 
            idx+=1
        total = 1
        for cnt in  dic.values(): 
            # ex) # headgear a개, eyewear b개일때, 경우의수 : a+b+a*b 
            total *= cnt+1
        # 출력 : n개의 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우
        print(total -1)

solution(data)