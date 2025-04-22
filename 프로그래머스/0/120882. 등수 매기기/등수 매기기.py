def solution(score):
    total = [a+b for a,b in score]
    sorted_total = sorted(total, reverse=True) 
    return [sorted_total.index(i)+1 for i in total]