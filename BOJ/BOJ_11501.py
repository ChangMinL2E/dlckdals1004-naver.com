# BOJ_11501 주식

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    total = 0
    N = int(input())
    Lst = list(map(int,input().split()))


    idx = 0
    while N-idx:
        max_i = Lst.index(max(Lst[idx:]))
        for i in range(idx,max_i+1):
            total += Lst[max_i]-Lst[i]

        idx = max_i+1

    print(total)

