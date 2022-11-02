# BOJ_10844 쉬운 계단 수

import sys
input = sys.stdin.readline

N = int(input())
Lst = [[0 for i in range(10)] for _ in range(101)]

for i in range(1,10):
    Lst[0][i] = 1 # 1,2,3,4,5,6,7,8,9

for row in range(1,100):
    for idx in range(10):
        if not idx:
            Lst[row][idx] = Lst[row-1][idx+1]
        elif idx == 9:
            Lst[row][idx] = Lst[row-1][idx-1]
        else:
            Lst[row][idx] = Lst[row-1][idx-1]+Lst[row-1][idx+1]

print(sum(Lst[N-1])%1000000000)





