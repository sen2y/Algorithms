dic = {
    'zero': '0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

def solution(numbers): 
    for i in dic.keys():
        sr = 'testtete te'  
        numbers = numbers.replace(i, dic[i]) 
    return int(numbers)
    