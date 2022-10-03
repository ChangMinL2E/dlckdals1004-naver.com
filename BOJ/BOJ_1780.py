# BOJ_1780 종이의 개수

# 좌측 상단 원소를 기준으로 잡고, 다른 순간 9등분 하자!


def divide(row,col,n):
    global zero,one,minus

    standard = Lst[row][col]
    for i in range(row,row+n):
        for j in range(col,col+n):
            if Lst[i][j] != standard:
                for k in range(3):
                    for l in range(3):
                        divide(row+k*n//3,col+l*n//3,n//3) # n by n -> n//3 by n//3
                return # 굳이 그 다음 요소를 볼 필요가 없다.

    if standard == 1:
        one += 1
    elif standard == 0:
        zero += 1
    else:
        minus += 1

    return

N = int(input())
zero, one,minus = 0,0,0
Lst = [list(map(int,input().split())) for _ in range(N)]

divide(0,0,N)
print(minus)
print(zero)
print(one)



