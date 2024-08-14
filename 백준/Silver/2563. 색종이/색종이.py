def main():
    grid = [[0] * 100 for _ in range(100)] 

    array = []
    n = int(input())
    for i in range(n):
        x, y = list(map(int, input().split())) 
        
        # 색종이 붙이기
        for i in range(x, x+10):
            for j in range(y, y+10):
                    grid[i][j] = 1;
    
    fill_cnt = 0;
    for i in range(100):
        for j in range(100):
            if grid[i][j] == 1 : 
                fill_cnt += 1

    print(fill_cnt)


main()