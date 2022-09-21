# BOJ_1004 기하1 어린왕자
import sys

Testcase = int(sys.stdin.readline())

for _ in range(Testcase):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    cnt = 0
    for _ in range(int(sys.stdin.readline())):
        a, b, r = map(int, sys.stdin.readline().split())
        d1 = ((x1 - a) ** 2 + (y1 - b) ** 2) ** 0.5
        d2 = ((x2 - a) ** 2 + (y2 - b) ** 2) ** 0.5

        if (d1 < r and d2 > r) or (d2 < r and d1 > r):
            cnt += 1

    print(cnt)
