# BOJ_6064 카잉 달력

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    M, N1, x, y = map(int, input().split())
    cml = True
    while x<= M*N1:
        if not (x-y)%N1:
            print(x)
            cml = False
            break
        x+=M

    if cml:
        print(-1)





