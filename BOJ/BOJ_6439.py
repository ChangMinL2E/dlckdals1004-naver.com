# BOJ_6439 교차 / Geometry

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x_st,y_st,x_ed,y_ed,x_left,y_top,x_right, y_bottom = map(int,input().split())

    if x_left < x_st < x_right and x_left < x_ed < x_right and y_bottom < y_st < y_top and y_bottom < y_ed < y_top:
        print('T')
    elif x_st == x_ed:
        if (x_st-x_left)*(x_st-x_right)<=0:
            print('T')
        else:
            print('F')
    else:
        a = (y_st-y_ed)/(x_st-x_ed)
        b = y_ed-a*x_ed
        if ((y_top - (a * x_right + b)) * (y_bottom - (a * x_left + b)) > 0) and ((y_top - (a * x_left + b)) * (y_bottom - (a * x_right + b)) > 0) and ((y_top - (a * x_left + b)) * (y_top - (a * x_right + b)) > 0) and ((y_bottom - (a * x_left + b)) * (y_bottom - (a * x_right + b)) > 0) :
            print('F')
        else:
            print('T')






