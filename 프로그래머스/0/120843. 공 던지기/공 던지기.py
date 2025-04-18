from itertools import cycle
def solution(numbers, k): 
    players = cycle(numbers) 
    cnt = 1
    for i in players: 
        if cnt == k: return i
        cnt+=1
        next(players)
        
        
            
        
                