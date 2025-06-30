import sys
input = sys.stdin.readline
T = int(input())
for k in range(T):
    n = int(input())
    result = []
    case = list(map(int, input().split()))
    case.sort()
    for i in case: 
        if i * (4/3) in case: result.append(i) 
        case.remove(int(i * (4/3)))
    print('Case #'+str(k+1)+': '+' '.join(map(str,result)))