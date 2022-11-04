# BOJ_11501 시간초과 뒤에서 부터 보자

# BOJ_11501 주식

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    total = 0
    N = int(input())
    Lst = list(map(int,input().split()))

    height = Lst[-1]
    for i in range(N-2,-1,-1):
        if Lst[i]>height:
            height = Lst[i]
        else:
            total += height-Lst[i]

    print(total)

