# 행, 열, 대각선 합중 최대 뽑기.

for tc in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    dia_max = 0
    r_dia_max = 0
    high = 0

    for i in range(100):
        row_max = 0
        for j in range(100):
            if i == 0:
                high += lst[i][j]
            else:
                row_max += lst[i][j]
        if row_max >= high:  # 행 최대값
            high = row_max

    for k in range(100):  # 열 최대값
        col_max = 0
        for l in range(100):
            col_max += lst[l][k]
        if col_max >= high:
            high = col_max

    for i in range(100):
        for j in range(100):
            if i == j:
                dia_max += lst[i][j]
                r_dia_max += lst[i][99 - j]

    if dia_max >= high:
        high = dia_max
    elif r_dia_max >= high:
        high = r_dia_max

    print(f'#{tc} {high}')
