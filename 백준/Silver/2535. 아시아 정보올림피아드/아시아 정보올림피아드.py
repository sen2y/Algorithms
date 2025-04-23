import sys
input = sys.stdin.read
data = input().rstrip().split('\n')

n = data[0]
data = data[1:]

def solution(data):
    arr = []
    for i in data:
        # 국가번호 a, 학생 번호 b, 성적 score
        a, b, score = map(int,i.split()) 
        arr.append([a,b,score]) 
    # 나라 별 메달 수는 최대 2개 
    sorted_arr = sorted(arr, key = lambda x: -x[2]) 
    cnt, country = 0, ''; 
    results = []
    for i in sorted_arr:  
        if cnt == 2 and i[0] == country: 
            continue 
       
        results.append(' '.join(map(str, i[:-1])))
        cnt +=1
        if country == '' : country = i[0]
        elif country != i[0]: country = '' 
        if len(results) == 3: 
            print('\n'.join(map(str, results)))
            return
        


solution(data)