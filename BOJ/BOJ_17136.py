# BOJ_17136 색종이 붙이기
import sys

input = sys.stdin.readline
from copy import deepcopy


def Backtracking(Visit, x, y, curCnt):
    global minimum
    if curCnt >= minimum:
        return

    if x == 9 and y == 9:
        if not Visit[9][9] and Papers[9][9]:
            curCnt += 1

        minimum = curCnt
        return
    # print(x,y)
    if not Papers[x][y] or Visit[x][y]:  # 종이를 안붙여도 되는 경우,
        if y == 9:  # 마지막 칸이면,
            Backtracking(Visit, x + 1, 0, curCnt)
        else:
            Backtracking(Visit, x, y + 1, curCnt)
    else:  # 붙여야 되는 경우가 오면,
        row_available = 5
        col_available = 5
        # if x <= 5 and y <= 5:
        #     row_available = 5
        #     col_available = 5
        # elif x <= 5:
        #     col_available = 10 - y
        # elif y <= 5:
        #     row_available = 10- x
        # else:
        #     row_available = 10 - x
        #     col_available = 10 - y

        for i in range(5):
            if 0<=x+i< 10:
                if Papers[x+i][y]:
                    for j in range(1, 5):
                        if 0 <= x + i < 10 and 0 <= y + j < 10:
                            # 셀껀데, 만약 종이가 붙어있거나, 종이를 애초에 붙일 필요가 없는 경우,
                            # if j != 0:
                            if j < col_available:  # 최소값을 찾았는데, 굳이 볼필요가 있나.
                                if Visit[x + i][y + j] or not Papers[x + i][y + j]:  # 붙일 필요가 없는 경우
                                    if col_available > j:
                                        col_available = j
                        else:
                            if col_available > j:
                                col_available = j
                else:
                    if row_available > i:
                        row_available = i
                    break
            else:
                if row_available > i:
                    row_available = i


        for j in range(col_available):
            for i in range(1, 5):
                if 0 <= x + i < 10 and 0 <= y + j < 10:
                    # 셀껀데, 만약 종이가 붙어있거나, 종이를 애초에 붙일 필요가 없는 경우,
                    # if i != 0:
                    if i < row_available:  # 최소값을 찾았는데, 굳이 볼필요가 있나.
                        if Visit[x + i][y + j] or not Papers[x + i][y + j]:  # 붙일 필요가 없는 경우
                            if row_available > i:
                                row_available = i
                else:
                    if row_available > i:
                        row_available = i

        available = min(row_available, col_available)
        for go in range(1, available + 1):
            if dic[go] != 0:
                dic[go] -= 1
                Visit2 = deepcopy(Visit)
                for id in range(go):
                    for jd in range(go):
                        Visit2[x + id][y + jd] = True
                if y + go >= 10:
                    Backtracking(Visit2, x + 1, 0, curCnt + 1)
                else:
                    Backtracking(Visit2, x, y + go, curCnt + 1)
                dic[go] += 1


visited = [[False] * 10 for _ in range(10)]
Papers = [list(map(int, input().split())) for _ in range(10)]
dic = {
    1: 5,
    2: 5,
    3: 5,
    4: 5,
    5: 5,
}
minimum = 1e10
Backtracking(visited, 0, 0, 0)

if minimum == 1e10:
    minimum = -1
print(minimum)


