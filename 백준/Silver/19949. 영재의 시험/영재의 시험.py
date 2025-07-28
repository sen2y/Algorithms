import sys
input = sys.stdin.readline

answers = list(map(int, input().split()))
result = 0

def dfs(idx, selected, correct, prev1, prev2):
    global result 
    if idx == 10:
        if correct >=5: result +=1
        return
    for choice in range(1, 6):
        if prev1 == prev2 == choice:
            continue
        is_correct = 1 if choice == answers[idx] else 0
        dfs(idx + 1, selected+[choice], correct + is_correct, prev2, choice)

dfs(0, [], 0,0,0)
print(result)