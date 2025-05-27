# 입력
import sys
input = sys.stdin.readline
# 첫 번째 줄에는 테스트 데이터의 수 정수 T
T = int(input())
# 각 테스트 데이터의 첫 번째 줄에는 팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 로그 엔트리의 개수 m
# 3 ≤ n, k ≤ 100, 1 ≤ t ≤ n, 3 ≤ m ≤ 10,000
for _ in range(T):
    n, k, t, m = map(int, input().split())

    list = [0]*(k+1)
    # 팀당 문제별 점수 저장
    scores = [[0]*(k+1) for _ in range(n+1)] 
    # 팀당 제출횟수
    submit_cnt = [0] * (n+1)
    # 팀당 마지막 제출 시간
    last_time = [0] * (n+1)
# 그 다음 m개의 줄에는 팀 ID i, 문제 번호 j, 획득한 점수 s
# 1 ≤ i ≤ n, 1 ≤ j ≤ k, 0 ≤ s ≤ 100 
    for time in range(m):
        i, j, s = map(int, input().split()) 
        # 최고 점수만 저장
        scores[i][j] = max(scores[i][j], s) 
        # 제출횟수 증가, 마지막 제출시간 기록
        submit_cnt[i] += 1
        last_time[i] = time
    # ranks = []
    # 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다. 
    # 마지막 제출 시간이 더 빠른 팀의 순위가 높다.
    ranks = sorted(range(1, n+1), key=lambda id:(
        -sum(scores[id]), submit_cnt[id], last_time[id], id))

# 출력
# 당신 팀의 순위를 한 줄에 출력
# 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다. 
# 마지막 제출 시간이 더 빠른 팀의 순위가 높다. 
# 당신 팀의 순위를 출력
    for idx, team_id in enumerate(ranks):
        if team_id == t: 
            print(idx+1)
            break