# BOJ_10828 스택
# Runtime_error

import sys
input = sys.stdin.readline
STK = []

for _ in range(int(input())):
    InputS = input().split()

    if InputS[0] == "pop":
        if len(STK) == 0:
            print(-1)
        else:
            print(STK.pop())
    elif InputS[0] == 'top':
        if len(STK) == 0:
            print(-1)
        else:
            print(STK[-1])
    elif InputS[0] == "empty":
        if len(STK) == 0:
            print(1)
        else:
            print(0)
    elif InputS[0] == 'size':
        print(len(STK))
    else:
        STK.append(int(InputS[-1]))


