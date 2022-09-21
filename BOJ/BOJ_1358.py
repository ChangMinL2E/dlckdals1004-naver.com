# BOJ_1358 기하 1 하키

import sys
W,H,X,Y,P = map(int,sys.stdin.readline().split())
r = H/2
cnt = 0
for _ in range(P):
    x,y = map(int,sys.stdin.readline().split())
    left_distance = ((x-X)**2+ (y-(Y+r))**2)**0.5
    right_distance = ((x-(X+W))**2 + (y-(Y+r))**2)**0.5
    if X<=x<=X+W and Y<=y<=Y+H:
        cnt += 1
    elif left_distance <= r:
        cnt += 1
    elif right_distance <= r:
        cnt += 1

print(cnt)




