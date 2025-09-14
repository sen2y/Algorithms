# 8:42
def solution(board, moves):
    n = len(board)
    board.reverse()
    # n개의 개별 스택을 만들어서, 뒤에서부터 stack으로 쌓고,
    stacks = [[] for _ in range(n)] 
    for line in board:
        for i in range(n): 
            if line[i] > 0: stacks[i].append(line[i])
    # 결과 스택에 하나씩 옮겨보기.
    print(stacks)  
    
    result = []
    cnt = 0
    for move in moves:
        if stacks[move-1]: 
            m = stacks[move-1].pop()
            if result and result[-1] == m:
                result.pop()
                cnt+=2
            else: result.append(m)
    
    # answer = 0
    print(result)
    return cnt