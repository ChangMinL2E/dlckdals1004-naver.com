# BOJ_1780 종이의 개수
import sys
sys.setrecursionlimit(500000)


def divide(lst,N):
    global zero,one,minus

    zero_cnt, one_cnt, minus_cnt = 0,0,0
    for i in range(N):
        zero_cnt += lst[i].count(0)
        one_cnt += lst[i].count(1)
        minus_cnt += lst[i].count(-1)

    if zero_cnt == N*N:
        zero += 1
        return

    elif one_cnt == N*N:
        one += 1
        return

    elif minus_cnt == N*N:
        minus += 1
        return

    else:
        if N != 3:
            for i in range(0,N,3): # 3등분
                for k in range(round(N/3)): # 열 숫자
                    new_lst = []
                    for j in range(round(N/3)): # 행 숫자
                        new_lst.append(lst[i+j][round(N/3)*k:round(N/3)*k+round(N/3)])
                    # new_lst 완성
                    divide(new_lst, round(N/3))
        else:
            for idx in range(3):
                for jdx in range(3):
                    if lst[idx][jdx] == 0:
                        zero += 1
                    elif lst[idx][jdx] == 1:
                        one += 1
                    else:
                        minus += 1
            return

Num = int(sys.stdin.readline())
zero, one,minus = 0,0,0
Lst = [list(map(int,sys.stdin.readline().split())) for _ in range(Num)]

divide(Lst,Num)
print(minus)
print(zero)
print(one)



