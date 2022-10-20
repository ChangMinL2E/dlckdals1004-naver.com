# BOJ_14868 문명
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
rep = []
for i in range(N):
    lst = []
    for j in range(N):
        lst.append((i,j))
    rep.append(lst)

def find_set(x):
    while x[0] != rep[x][0] or x[1] != rep[x][1]:
        x[0],x[1] = rep[x][1], rep[x][1]
    return x

def Union(x,y):
    if find_set(x)[0]<find_set(y)[0]:
        rep[find_set(y)] = find_set(x)
    elif find_set(x)[0] == find_set(y)[0] and find_set(x)[1] < find_set(y)[1]:
        rep[find_set(y)] = find_set(x)
    else:
        rep[find_set(x)] = find_set(y)

Lst = []
for _ in range(K):
    a,b = map(int,input().split())
    Lst.append([a-1,b-1])

delta = [(1,0),(-1,0),(0,1),(0,-1)]
Queue = deque([])

for ls in Lst:
    for dt in delta:
        x,y = ls[0]+dt[0],ls[1]+dt[1]
        if 0<=x<N and 0<=y<N and rep[x][y] == [x,y] and not [x,y] in Lst:
            rep[x][y] = (ls[0],ls[1])
            Queue.append([x,y])
        elif 0<=x<N and 0<=y<N and rep[x][y] != [x,y]: # 이미 방문한 문명이 있다면,
            Union([x,y],ls)
            Queue.append([x,y])
for ls in Lst:
    if find_set(Lst[0]) != find_set(ls):
        break
else:
    print(1)

cnt = 1


