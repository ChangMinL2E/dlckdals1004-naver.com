# BOJ_12781 PIZZA ALVOLOC

import sys
input = sys.stdin.readline

x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
if x1 == x2:
    if (x4-x1)*(x3-x1) < 0:
        print(1)
    else:
        print(0)

    # a = (y4-y3)/(x4-x3)
    # b = y3 - a*x3
    #
    # if (y1-(a*x1+b))*(y2-(a*x2+b)) < 0:
    #     print(1)
    # else:
    #     print(0)
else:
    a = (y2-y1)/(x2-x1)
    b = y1 - a*x1
    if (y3 - (a * x3 + b)) * (y4 - (a * x4 + b)) < 0:
        print(1)
    else:
        print(0)





