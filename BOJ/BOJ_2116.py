# BOJ 2116 주사위 쌓기
# 다시 생각하고 손코딩 끝나면 시작하기.

dice_cnt = int(input())
dices = []
for _ in range(dice_cnt):
    dice = list(map(int,input().split()))
    dice[3], dice[4], dice[5] = dice[5], dice[3], dice[4] # 짝 맞추기.
    # A-F, B-D, C-E
    dices.append(dice) # 주사위 모음 생성

lst = []
top = 0 # 윗면
bottom = 0 # 아랫면


for i in range(len(dices)):
    if i != 0:
        bottom_idx = dices[i].index(top)
        bottom = dices[i][bottom_idx]





    elif i == 0:
        idx = dices[i].index(6) # 6의 인덱스
        one_idx = dices[i].index(1)
        lst.append(6)
        if one_idx%3 != idx%3:
            top = 1
        else:
            top = 2


    # print(idx)#





