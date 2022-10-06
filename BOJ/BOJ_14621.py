# BOJ_14621 나만 안되는 연애

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)] = find_set(x)

N, M = map(int,input().split())
gender = input().split()
edge = [list(map(int,input().split())) for _ in range(M)]
rep = [x for x in range(N+1)]
edge.sort(key=lambda x:x[2])

cnt = 0
total = 0

for st, ed, weight in edge:
    if find_set(st) != find_set(ed) and gender[st-1] != gender[ed-1]:
        cnt += 1
        total += weight
        Union(st,ed)

    if cnt == N-1:
        break
if cnt == N-1:
    print(total)
else:
    print(-1)








