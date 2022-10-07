# BOJ_16398 행성연결 / MST

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)] = find_set(x)

N = int(input())
visited = [False]*N
Lst = [list(map(int,input().split())) for _ in range(N)]

edge = []
for i in range(N):
    for j in range(N):
        if i != j:
            edge.append((i,j,Lst[i][j]))

edge.sort(key=lambda x: x[2])
rep = [x for x in range(N)]
cnt = 0
total = 0

for st, ed, weight in edge:
    if find_set(st) != find_set(ed):
        cnt += 1
        total += weight
        Union(st,ed)

    if cnt == N-1:
        break

print(total)



