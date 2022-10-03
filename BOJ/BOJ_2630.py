# BOJ_2630 색종이 만들기 / 분할 정복

def divide(row, col, n):
    global white, blue

    standard = Papers[row][col]
    for i in range(n):
        for j in range(n):
            if Papers[row+i][col+j] != standard:
                for k in range(2):
                    for l in range(2):
                        divide(row+k*n//2, col+l*n//2, n//2)
                return

    if standard == 0:
        white += 1
    else:
        blue += 1
    return

N = int(input())
Papers = [list(map(int,input().split())) for _ in range(N)]
white = 0
blue = 0
divide(0,0,N)
print(white)
print(blue)


