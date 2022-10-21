# BOJ_17386 선분 교차 1

import sys
input = sys.stdin.readline

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

if x1!=x2 and x3!=x4:
    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    c = (y4-y3)/(x4-x3)
    d = y3-c*x3
    if a == c:
        print(0)
    else: # 평행하지 않으면,
        cross_x = (d-b)/(a-c)
        cross_y =  a*cross_x+b
        if x1 > x2:
            x2, x1 = x1, x2
        if x3 > x4:
            x4, x3 = x3, x4
        if y1 > y2:
            y1 , y2 = y2, y1
        if y3 > y4:
            y3, y4 = y4, y3

        if (x1-(1e-10)<=cross_x<=x2+(1e-10) and y1-(1e-10)<=cross_y<=y2+(1e-10)) and (x3-(1e-10)<=cross_x<=x4+(1e-10) and y3-(1e-10)<=cross_y<=y4+(1e-10)): # 선분 위에 존재
            print(1)
        else: # 존재 하지 않는다면,
            print(0)



elif x1==x2 and x3==x4:
    print(0)
elif x1 == x2: # y축에 평행한 직선이라면,
    c = (y4-y3)/(x4-x3)
    d = y3-c*x3
    cross_y = c*x1+d
    if y1 > y2:
        y1,y2 = y2,y1

    if y1-(1e-10) < cross_y < y2+(1e-10):
        print(1)
    else:
        print(0)
elif x3 == x4:
    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    cross_y = a*x3+b
    if y3 > y4:
        y3,y4 = y4,y3

    if y3-(1e-10) < cross_y < y4+(1e-10):
        print(1)
    else:
        print(0)





