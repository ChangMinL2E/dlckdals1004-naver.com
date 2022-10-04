# BOJ_2887 행성 터널 / MST
# 모든 간선을 보면 메모리 초과 된다.

import sys
input = sys.stdin.readline

def minimum_cost(x,y):
    return min(abs(x[0]-y[0]),abs(x[1]-y[1]),abs(x[2]-y[2]))

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)] = find_set(x)

V = int(input())
points = [tuple(map(int,input().split())) for _ in range(V)]

edge = []
for i in range(V-1):
    for j in range(V):
        edge.append((i,j,minimum_cost(points[i],points[j])))

rep = [x for x in range(V)]

cnt = 0
total = 0

edge.sort(key=lambda x:x[2])

for st, ed, weight in edge:
    if find_set(st) != find_set(ed):
        cnt += 1
        total += weight
        Union(st,ed)

    if cnt == V-1:
        break

print(total)







