# BOJ_13459 구슬 탈출

import sys

input = sys.stdin.readline

def Backtracking(Red, Blue, button, cnt):
    global minimum

    if minimum < cnt:
        return

    if cnt > 10:
        return

    if button == 1:  # 빨강 공만 들어가는 경우
        if minimum > cnt:
            minimum = cnt
        return

    if button == 2:  # 파랑 공이 들어가는 경우
        return

    # 오른쪽부터 기울여보자. / 열이 큰거부터,
    if Blue[1] > Red[1]:  # 퍼런 공이 오른쪽에 있다면,
        x = Blue[0]
        blue_y = Blue[1]
        for j in range(1, M):
            y = Blue[1] + j
            if 0 <= y < M:
                if Lst[x][y] == '.':
                    blue_y = y
                elif Lst[x][y] == 'O':
                    x, blue_y = 11, 11
                    button = 2
                    break
                else:
                    break
        Blue_right = (x, blue_y)

        x = Red[0]
        red_y = Red[1]
        for j in range(1, M):
            y = Red[1] + j
            if 0 <= y < M:
                if Lst[x][y] == '.' and (x, y) != Blue_right:
                    red_y = y
                elif Lst[x][y] == 'O' and not button:  # 먼저 들어가야 함.
                    button = 1
                    x, red_y = 11, 11
                    break
                else:
                    break
        Red_right = (x, red_y)
    else:  # 빨강 공이 오른쪽에 있다면,
        x = Red[0]
        red_y = Red[1]
        for j in range(1, M):
            y = Red[1] + j
            if 0 <= y < M:
                if Lst[x][y] == '.':
                    red_y = y
                elif Lst[x][y] == 'O' and not button:
                    x, red_y = 11, 11
                    button = 1
                    break
                else:
                    break
        Red_right = (x, red_y)

        x = Blue[0]
        blue_y = Blue[1]
        for j in range(1, M):
            y = Blue[1] + j
            if 0 <= y < M:
                if Lst[x][y] == '.' and (x, y) != Red_right:
                    blue_y = y
                elif Lst[x][y] == 'O':
                    button = 2
                    x, blue_y = 11, 11
                    break
                else:
                    break
        Blue_right = (x, blue_y)
    # 오른쪽 경우 슈웃
    Backtracking(Red_right, Blue_right, button, cnt + 1)
    button = 0
    # 2. 왼쪽 / 열이 작은거부터,
    if Blue[1] < Red[1]:  # 퍼런 공이 왼쪽에 있다면,
        x = Blue[0]
        blue_y = Blue[1]
        for j in range(1, M):
            y = Blue[1] - j
            if 0 <= y < M:
                if Lst[x][y] == '.':
                    blue_y = y
                elif Lst[x][y] == 'O':
                    x, blue_y = 11, 11
                    button = 2
                    break
                else:
                    break
        Blue_left = (x, blue_y)

        x = Red[0]
        red_y = Red[1]
        for j in range(1, M):
            y = Red[1] - j
            if 0 <= y < M:
                if Lst[x][y] == '.' and (x, y) != Blue_left:
                    red_y = y
                elif Lst[x][y] == 'O' and not button:
                    button = 1
                    x, red_y = 11, 11
                    break
                else:
                    break
        Red_left = (x, red_y)

    else:  # 빨강 공이 왼쪽에 있다면,
        x = Red[0]
        red_y = Red[1]
        for j in range(1, M):
            y = Red[1] - j
            if 0 <= y < M:
                if Lst[x][y] == '.':
                    red_y = y
                elif Lst[x][y] == 'O' and not button:
                    x, red_y = 11, 11
                    button = 1
                    break
                else:
                    break
        Red_left = (x, red_y)

        x = Blue[0]
        blue_y = Blue[1]
        for j in range(1, M):
            y = Blue[1] - j
            if 0 <= y < M:
                if Lst[x][y] == '.' and (x, y) != Red_left:
                    blue_y = y
                elif Lst[x][y] == 'O':
                    button = 2
                    x, blue_y = 11, 11
                    break
                else:
                    break
        Blue_left = (x, blue_y)

    # 왼쪽 경우 슈웃
    Backtracking(Red_left, Blue_left, button, cnt + 1)
    button = 0
    # 3. 위쪽 경우
    if Blue[0] < Red[0]:  # 퍼런 공이 위에 있다면,
        y = Blue[1]
        blue_x = Blue[0]
        for j in range(1, N):
            x = Blue[0] - j
            if 0 <= x < N:
                if Lst[x][y] == '.':
                    blue_x = x
                elif Lst[x][y] == 'O':
                    blue_x, y = 11, 11
                    button = 2
                    break
                else:
                    break
        Blue_top = (blue_x, y)

        y = Red[1]
        red_x = Red[0]
        for j in range(1, N):
            x = Red[0] - j
            if 0 <= x < N:
                if Lst[x][y] == '.' and (x, y) != Blue_top:
                    red_x = x
                elif Lst[x][y] == 'O' and not button:
                    red_x, y = 11, 11
                    button = 1
                    break
                else:
                    break
        Red_top = (red_x, y)

    else:  # 뻘건 공이 위에 있다면,
        y = Red[1]
        red_x = Red[0]
        for j in range(1, N):
            x = Red[0] - j
            if 0 <= x < N:
                if Lst[x][y] == '.':
                    red_x = x
                elif Lst[x][y] == 'O' and not button:
                    red_x, y = 11, 11
                    button = 1
                    break
                else:
                    break
        Red_top = (red_x, y)

        y = Blue[1]
        blue_x = Blue[0]
        for j in range(1, N):
            x = Blue[0] - j
            if 0 <= x < N:
                if Lst[x][y] == '.' and (x, y) != Red_top:
                    blue_x = x
                elif Lst[x][y] == 'O':
                    blue_x, y = 11, 11
                    button = 2
                    break
                else:
                    break
        Blue_top = (blue_x, y)

    # 위쪽 경우 슈웃
    Backtracking(Red_top, Blue_top, button, cnt + 1)
    button = 0
    # 4. 아래쪽 경우

    if Blue[0] > Red[0]:  # 퍼런 공이 아래에 있다면,
        y = Blue[1]
        blue_x = Blue[0]
        for j in range(1, N):
            x = Blue[0] + j
            if 0 <= x < N:
                if Lst[x][y] == '.':
                    blue_x = x
                elif Lst[x][y] == 'O':
                    blue_x, y = 11, 11
                    button = 2
                    break
                else:
                    break
        Blue_bottom = (blue_x, y)

        y = Red[1]
        red_x = Red[0]
        for j in range(1, N):
            x = Red[0] + j
            if 0 <= x < N:
                if Lst[x][y] == '.' and (x, y) != Blue_bottom:
                    red_x = x
                elif Lst[x][y] == 'O' and not button:
                    red_x, y = 11, 11
                    button = 1
                    break
                else:
                    break
        Red_bottom = (red_x, y)

    else:  # 뻘건 공이 위에 있다면,
        y = Red[1]
        red_x = Red[0]
        for j in range(1, N):
            x = Red[0] + j
            if 0 <= x < N:
                if Lst[x][y] == '.':
                    red_x = x
                elif Lst[x][y] == 'O' and not button:
                    red_x, y = 11, 11
                    button = 1
                    break
                else:
                    break
        Red_bottom = (red_x, y)

        y = Blue[1]
        blue_x = Blue[0]
        for j in range(1, N):
            x = Blue[0] + j
            if 0 <= x < N:
                if Lst[x][y] == '.' and (x, y) != Red_bottom:
                    blue_x = x
                elif Lst[x][y] == 'O':
                    blue_x, y = 11, 11
                    button = 2
                    break
                else:
                    break
        Blue_bottom = (blue_x, y)

    # 아래쪽 경우 슈웃
    Backtracking(Red_bottom, Blue_bottom, button, cnt + 1)
    button = 0

N, M = map(int, input().split())
Lst = [list(input().strip()) for _ in range(N)]
minimum = 11
red = 0
blue = 0
for i in range(N):
    for j in range(M):
        if Lst[i][j] == 'R':
            red = (i, j)
            Lst[i][j] = '.'
        elif Lst[i][j] == 'B':
            blue = (i, j)
            Lst[i][j] = '.'

Backtracking(red, blue, 0, 0)
if minimum == 11:
    print(0)
else:
    print(1)







