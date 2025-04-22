def solution(chicken): 
    service = 0
    coupon = chicken
    while coupon >= 10:
        free = coupon // 10
        service += free
        coupon = coupon%10 + free
    return service
        