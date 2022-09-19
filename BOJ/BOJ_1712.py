# BOJ_1712 손익분기점

A, x,y = map(int,input().split())

if y-x <= 0:
    print(-1)
else:
    print(A//(y-x)+1)