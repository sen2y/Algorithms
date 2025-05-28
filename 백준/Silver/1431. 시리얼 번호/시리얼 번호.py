# 입력
# 첫째 줄에 기타의 개수 N <= 50
# 둘째 줄부터 N개의 줄에 시리얼 번호, 알파벳 대문자 또는 숫자로만, 중복되지 않는다.
import sys
input = sys.stdin.readline

N = int(input())  

arr = [input().rstrip() for _ in range(N)]  
# 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
def digit_sum(line):
    return sum(int(i) for i in line if i.isdigit()) 
# 길이가 다르면, 짧은 것이 먼저
# 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
arr.sort(key=lambda x:(len(x), digit_sum(x), x))

# 출력
# N개의 줄에 한줄에 하나씩 시리얼 번호를 정렬한 결과
print('\n'.join(arr))
