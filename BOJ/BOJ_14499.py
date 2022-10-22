# BOJ_14499 주사위 굴리기
import sys
imput = sys.stdin.readline
from collections import deque

dice = [0]*7
row,col,x,y,N = map(int,input().split())
Lst = [list(map(int,input().split())) for _ in range(row)]
directions = deque(list(map(int,input().split())))
dic = {
    1:(0,1),
    2:(0,-1),
    3:(-1,0),
    4:(1,0)
}

while directions:
    direct = directions.popleft()
    if 0<= x+dic[direct][0] < row and 0<= y+dic[direct][1] < col:
        x,y = x+dic[direct][0], y+dic[direct][1]

        # 주사위 숫자 바꾸기
        if direct == 3: # 위로 굴리면,
            temp = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[6]
            dice[6] = dice[5]
            dice[5] = temp
        elif direct == 4: # 아래로 굴리면,
            temp = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[6]
            dice[6] = dice[2]
            dice[2] = temp
        elif direct == 1: # 오른쪽으로 굴리면,
            temp = dice[1]
            dice[1] = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            dice[4] = temp
        else: # 왼쪽으로 굴리면,
            temp = dice[1]
            dice[1] = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            dice[3] = temp

        # 자리 다 바꿨으면 바닥면 비교해주기!

        if Lst[x][y]:
            dice[1] = Lst[x][y]
            Lst[x][y] = 0
        else: # 칸이 0,
            Lst[x][y] = dice[1]

        print(dice[6])




