# BOJ_1992 쿼드트리

def divide(row, col, n):

    standard = Lst[row][col]
    for i in range(n):
        for j in range(n):
            if Lst[row+i][col+j] != standard:
                print('(', end='')
                for k in range(2):
                    for l in range(2):
                        divide(row+k*n//2, col+l*n//2, n//2)
                print(')',end='')
                return

    if Lst[row][col] == 0:
        print(0,end='')
    else:
        print(1,end='')
    return



N = int(input())
Lst = [list(map(int,input())) for _ in range(N)]
divide(0,0,N)





