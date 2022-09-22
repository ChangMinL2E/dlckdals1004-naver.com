# BOJ_2580 백트래킹 스도쿠
# 시간초과

import sys

lst = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
# lst = [list(map(int, input().split())) for _ in range(9)]
zero_count = 0
# print(lst)
for ls in lst:
    for ele in ls:
        if ele == 0:
            zero_count += 1

while zero_count:
    # 가로
    for idx in range(9):
        cnt = [0]*9
        zero_idx = 0
        zero_cnt = 0
        if lst[idx].count(0) == 1:
            for i in range(len(lst[idx])):
                if lst[idx][i]:
                    cnt[lst[idx][i]-1] += 1
                else:
                    zero_idx = i
                    zero_cnt += 1
            if zero_cnt == 1:
                for num in range(9):
                    if not cnt[num]:
                        lst[idx][zero_idx] = num+1
                        zero_count -= 1

    # 세로
    for jdx in range(9):
        cnt = [0]*9
        zero_idx = 0
        zero_cnt = 0
        for i in range(9):
            if lst[i][jdx]:
                cnt[lst[i][jdx]-1] += 1
            else:
                zero_idx = i
                zero_cnt += 1
        if zero_cnt == 1:
            for num in range(9):
                if not cnt[num]:
                    lst[zero_idx][jdx] = num+1
                    zero_count -= 1


    # 3곱하기 3
    for i in range(3):
        for j in range(3):
            cnt = [0]*9
            zero_cnt = 0
            for x_idx in range(3):
                for y_idx in range(3):
                    number = lst[3*i+x_idx][3*j+y_idx]
                    if number != 0:
                        cnt[number-1] += 1
                    else:
                        zero_idx = (3*i+x_idx, 3*j+y_idx)
                        zero_cnt += 1
            if zero_cnt == 1:
                for n in range(9):
                    if not cnt[n]:
                        lst[zero_idx[0]][zero_idx[1]] = n+1
                        zero_count -= 1

for ls in lst:
    print(*ls)








