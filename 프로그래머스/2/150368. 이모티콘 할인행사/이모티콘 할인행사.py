from itertools import product

def solution(users, emoticons):
    discount = [10,20,30,40]
    combs = [comb for comb in product(discount, repeat = len(emoticons))] 
    
    answer = [0, 0]
    for comb in combs:
        
        sub, sale = 0, 0
        # user마다 
        for rate, maxp in users:
            # print(999)
            price = 0
            # 각 조합별 가격체크
            for c, p in zip(comb, emoticons):
                if c<rate: continue
                saleprice = p * (100 - c) // 100
                price += saleprice
                # print(1, saleprice)
                
            # print(2, c, rate,price)
            if price >= maxp: # 구독한다
                sub += 1
                # print(3, sub, sale)
            else: 
                sale += price
                # print(4, sub, sale)
        if (answer[0] < sub) or ((answer[0] == sub) and  answer[1] < sale): 
            answer = [sub, sale]
            # print(5, answer) 
        
    
    
    return answer