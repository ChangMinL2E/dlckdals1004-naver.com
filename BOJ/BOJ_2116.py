# BOJ 2116 주사위 쌓기
# 다시 생각하고 손코딩 끝나면 시작하기.

dice_cnt = int(input())
dices = []
for _ in range(dice_cnt):
    dice = list(map(int,input().split()))
    dice[3], dice[4], dice[5] = dice[5], dice[3], dice[4] # 짝 맞추기.
    # A-F, B-D, C-E
    dices.append(dice) # 주사위 모음 생성

score_lst = [0,0,0,0,0,0]

# print(dices)
for idx in range(6): # 첫번째 주사위경우의 수에 따라 정해졌다.
    total = 0 # 경우의 수 별 총 합
    N = dice_cnt # 주사위 갯수.
    lst = []

    # 첫번째
    if N == dice_cnt:
        lst = dices[0]
        i = idx
        if i < 3:
            i_match = i+3
        else:
            i_match = i-3

        if lst[i] != 6 and lst[i_match] != 6:
            total += 6
        elif lst[i] == 6 and lst[i_match] != 5:
            total += 5
        elif lst[i_match] == 6 and lst[i] != 5:
            total += 5
        elif lst[i] == 6 and lst[i_match] == 5:
            total += 4
        elif lst[i] == 5 and lst[i_match] == 6:
            total += 4

        bottom = lst[i_match] # 다음 아랫면
        N = N-1

    # 2번째부터 마지막

    while N != 0:
        dice_i = dice_cnt-N
        lst = dices[dice_i]
        i = lst.index(bottom)
        if i < 3:
            i_match = i+3
        else:
            i_match = i-3

        if lst[i] != 6 and lst[i_match] != 6:
            total += 6
        elif lst[i] == 6 and lst[i_match] != 5:
            total += 5
        elif lst[i_match] == 6 and lst[i] != 5:
            total += 5
        elif lst[i] == 6 and lst[i_match] == 5:
            total += 4
        elif lst[i] == 5 and lst[i_match] == 6:
            total += 4

        bottom = lst[i_match] # 다음 아랫면
        N = N-1

    score_lst[idx] += total

print(max(score_lst))



