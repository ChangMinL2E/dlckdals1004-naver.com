# BOJ_17136 색종이 붙이기
# 리발 깨달았다.
import sys

input = sys.stdin.readline
from copy import deepcopy

def Backtracking(paper, x, y, curCnt):
    global minimum

    if curCnt >= minimum:
        return

    if x == 9 and y == 10:
        if minimum > curCnt:
            minimum = curCnt
        return

    if not paper[x][y]:  # 종이를 안붙여도 되는 경우,
        if y >= 9 and x <= 8:  # 마지막 칸이면,
            Backtracking(paper, x + 1, 0, curCnt)
        else:
            Backtracking(paper, x, y + 1, curCnt)
    else:  # 붙여야 되는 경우가 오면, default
        available = 5
        cml = True
        for i in range(1,available+1):
            for k_x in range(i):
                for k_y in range(i):
                    if 0<=x+k_x<10 and 0<=y+k_y<10:
                        if not paper[x+k_x][y+k_y]:
                            available = i-1
                            cml = False
                            break
                    else: # 범위 벗어나면,
                        available = i - 1
                        cml = False
                        break

                if not cml:
                    break
            if not cml:
                break

        for go in range(1, available + 1):
            if dic[go] != 0:
                dic[go] -= 1
                paper2 = deepcopy(paper)
                for id in range(go):
                    for jd in range(go):
                        paper2[x + id][y + jd] = 0
                if y + go >= 10 and x <= 8:
                    Backtracking(paper2, x + 1, 0, curCnt + 1)
                else:
                    Backtracking(paper2, x, y + go, curCnt + 1)
                dic[go] += 1


Papers = [list(map(int, input().split())) for _ in range(10)]
dic = {
    1: 5,
    2: 5,
    3: 5,
    4: 5,
    5: 5,
}
minimum = 1e10
Backtracking(Papers, 0, 0, 0)

if minimum == 1e10:
    minimum = -1
print(minimum)


