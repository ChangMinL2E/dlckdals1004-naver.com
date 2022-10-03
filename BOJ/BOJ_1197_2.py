# BOJ_1197 MST
# Kruskal 로 풀어보자.

def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)] = rep[find_set(x)]

V, E = map(int,input().split())
edge = [list(map(int,input().split())) for _ in range(E)]
rep = [x for x in range(V+1)]

cnt = 0
total = 0
edge.sort(key=lambda x:x[2])

for st,ed, weight in edge:
    if find_set(st) != find_set(ed): # cycle이 안되면,
        cnt += 1
        total += weight
        Union(st,ed)

    if cnt == V-1:
        break

print(total)
# print(edge)












