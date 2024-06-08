# 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return
def solution(angle):
    answer = 0
    if (angle > 0 and angle < 90): return 1
    elif(angle == 90): return 2
    elif(angle > 90 and angle < 180): return 3
    elif(angle == 180): return 4 