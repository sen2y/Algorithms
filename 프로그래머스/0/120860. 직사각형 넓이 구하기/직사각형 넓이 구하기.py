def solution(dots):  
    sorted_dots = sorted(dots)
    print(sorted_dots)
    return (abs(sorted_dots[2][0]-sorted_dots[0][0]) * abs(sorted_dots[1][1]-sorted_dots[0][1]))
        
        