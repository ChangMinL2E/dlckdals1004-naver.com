# BOJ_1002 기하 터렛
import sys

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 7)
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)

    elif d > r1+r2:
        print(0)
    elif d == r1+r2:
        print(1)
    elif d < r1+r2:
        if d > abs(r1-r2):
            print(2)
        elif d == abs(r1-r2):
            print(1)
        else:
            print(0)





