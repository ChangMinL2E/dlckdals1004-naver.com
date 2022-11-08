# BOJ_2231 분해합

import sys
input = sys.stdin.readline

N = int(input())
for number in range(1,N+1):
    N2 = number

    for i in str(number):
        N2 += int(i)
    if N2 == N:
        print(number)
        break

    if number == N:
        print(0)





