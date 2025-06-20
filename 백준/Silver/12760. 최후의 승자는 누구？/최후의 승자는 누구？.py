import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = [sorted(map(int, input().split()),reverse=True) for _ in range(N)]
scores = [0] * N

for i in range(M):
    max_num = max(cards[j][i] for j in range(N))
    for j in range(N):
        if cards[j][i] == max_num: scores[j] += 1

max_score = max(scores) 
result = [str(idx+1) for idx, score in enumerate(scores) if score == max_score]
print(' '.join(result))