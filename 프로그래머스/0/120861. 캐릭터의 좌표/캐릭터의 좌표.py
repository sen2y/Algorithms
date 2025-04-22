directions = {
    "left": (-1, 0),
    "right": (1, 0),
    "up": (0, 1),
    "down": (0, -1)
    }

def solution(keyinput, board): 
    # board의 정중앙 0,0에서 시작
    x, y = 0,0
    x_limit = board[0] // 2
    y_limit = board[1] // 2

    # board의 크기를 벗어난 방향키 입력은 무시
    for i in keyinput: 
        dx, dy = directions[i]
        nx, ny = x + dx, y + dy
        if -x_limit <= nx <= x_limit:
            x = nx
        if -y_limit <= ny <= y_limit:
            y = ny
    return [x,y]
     
# 반례 ["right", "right", "right", "right", "right", "left"], [9, 5]
solution( ["right", "right", "right", "right", "right", "left"], [9, 5])