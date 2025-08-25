import sys
input = sys.stdin.readline

S = input().strip()

cnts = [-1] * 26 # 아스키코드 a: 97, 문자열을 아스키로 변환: ord() 반대는 chr()
for idx, i in enumerate(S):
    # print(idx)
    if cnts[ord(i)-97] == -1: cnts[ord(i)-97] = idx
print(' '.join(map(str,cnts)))