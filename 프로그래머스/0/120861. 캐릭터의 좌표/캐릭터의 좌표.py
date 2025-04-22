range = {
        "left": [-1, 0],
        "right": [1, 0],
        "up": [0,1],
        "down": [0,-1]
    }

def solution(keyinput, board):
    print(keyinput, board)
    result = [0,0]  
    # board의 정중앙 0,0에서 시작
    # board의 크기를 벗어난 방향키 입력은 무시
    for i in keyinput: 
        if abs(result[0]+range[i][0]) <= board[0]//2: result[0] += range[i][0]
        if abs(result[1]+range[i][1]) <= board[1]//2: result[1] += range[i][1]
    return result
     
# 반례 ["right", "right", "right", "right", "right", "left"], [9, 5]
solution( ["right", "right", "right", "right", "right", "left"], [9, 5])