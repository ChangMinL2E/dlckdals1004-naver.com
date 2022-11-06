# BOJ_1018 체스판 다시 칠하기

import sys
input = sys.stdin.readline

def recursion(x,y,k,curSum):
    global minimum

    # if minimum <= curSum and minimum <= 64-curSum:
    #     return

    if k == 8:
        if minimum > min(curSum,64-curSum):
            minimum = min(curSum,64-curSum)
        return

    total = 0

    if not k%2: # 홀수 번째 열 'WBWBWBWB' 기준
        for idx in range(8):
            if idx % 2:# W
                if Lst[x+k][y:y+8][idx] == 'B':
                    total += 1
            else:
                if Lst[x + k][y:y + 8][idx] == 'W':
                    total += 1
    else:
        for idx in range(8):
            if idx % 2:
                if Lst[x+k][y:y+8][idx] == 'W':
                    total += 1
            else:
                if Lst[x + k][y:y + 8][idx] == 'B':
                    total += 1

    recursion(x,y,k+1,curSum+total)


N,M = map(int,input().split())
minimum = 64

Lst = [list(input()) for _ in range(N)]

for i in range(N-7):
    for j in range(M-7):
        recursion(i,j,0,0)

print(minimum)


