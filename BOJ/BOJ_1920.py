# BOJ_1920 수 찾기

import sys
input = sys.stdin.readline

N = int(input())
Lst = sorted(list(map(int,input().split())))
M = int(input())
lst = list(map(int,input().split()))

i = 0
for ls in lst:
    # for idx in range(N):
    #     if Lst[idx] == ls:
            # i = idx
            # print(1)
            # break
    if ls in Lst:
        print(1)

        # elif Lst[idx] > ls:
        #     print(0)
        #     break
        # elif Lst[-1] < ls:
        #     print(0)
        #     i = N-1
        #     break
    else:
        print(0)









