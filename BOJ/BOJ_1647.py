# BOJ_1647 도시 분할 계획
import sys
input = sys.stdin.readline

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)] = find_set(x)

V, E = map(int,input().split())
rep = [x for x in range(V+1)]
edge = [list(map(int,input().split())) for _ in range(E)]

edge.sort(key=lambda x: x[2])

cnt = 0
total = 0

for st, ed, weight in edge:
    if find_set(st) != find_set(ed):
        cnt += 1
        total += weight
        Union(st,ed)

    if cnt == V-2:
        break

print(total)

