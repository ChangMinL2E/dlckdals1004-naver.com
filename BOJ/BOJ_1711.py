# BOJ_1711 직각 삼각형

import sys
input = sys.stdin.readline

def triangle(a,b,c):
    if abs(((a[0]-b[0])**2 + (a[1]-b[1])**2)+((a[0]-c[0])**2 + (a[1]-c[1])**2) - ((c[0]-b[0])**2 + (c[1]-b[1])**2)) <= 1e-10:
        return 1
    elif abs(((a[0]-b[0])**2 + (a[1]-b[1])**2)-((a[0]-c[0])**2 + (a[1]-c[1])**2) + ((c[0]-b[0])**2 + (c[1]-b[1])**2)) <= 1e-10:
        return 1
    elif abs(-((a[0]-b[0])**2 + (a[1]-b[1])**2)+((a[0]-c[0])**2 + (a[1]-c[1])**2) + ((c[0]-b[0])**2 + (c[1]-b[1])**2)) <= 1e-10:
        return 1
    else:
        return 0

N = int(input())
Lst = [tuple(map(float,input().split())) for _ in range(N)]
Lst = list(set(Lst))
N = len(Lst)

cnt = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            cnt += triangle(Lst[i],Lst[j],Lst[k])
print(cnt)


