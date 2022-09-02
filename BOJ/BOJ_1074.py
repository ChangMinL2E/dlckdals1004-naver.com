# BOJ_1074 Z
# 시간초과.

N, r, c = map(int,input().split())

x_st, x_ed = 0, 2**(N)-1
y_st, y_ed = 0, 2**(N)-1

a = 1
b = 2**(2*N)

cml = True

if a == 0 and b == 0:
    cml = False
    a = 0

while cml:
    if r > (y_st+y_ed)//2:
        y_st = (y_st+y_ed)//2
        a = (a+b) // 2
    else:
        y_ed = (y_st + y_ed) // 2
        b = (a + b) // 2

    if c > (x_st+x_ed) // 2:
        x_st = (x_st+x_ed)//2
        a = (a+b) // 2
    else:
        x_ed = (x_st + x_ed) // 2
        b = (a + b) // 2

    if a+1 == b:
        cml = False

print(a)