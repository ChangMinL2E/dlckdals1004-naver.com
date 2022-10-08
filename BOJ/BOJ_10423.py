# BOJ_10423 전기가 부족해 / MST

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)]= find_set(x)


N, M, K = map(int,input().split())

rep = [x for x in range(N+1)]
Good = list(map(int,input().split())) # 발전소 위치

for g in Good:
    rep[g] = 0

edge = [list(map(int,input().split())) for _ in range(M)]
total = 0
cnt = 0
edge.sort(key=lambda x:x[2])
# test_lst = []

for st,ed, weight in edge:
    if find_set(st) != find_set(ed):
        # if visited[st] == False or visited[ed] == False:
        cnt += 1
        total += weight
        Union(st,ed)
        # test_lst.append((st,ed,weight))
            # visited[st] = True
            # visited[ed] = True

    # if cnt == N-K:
    #     break

print(total)
# print(test_lst)





[(7, 9, 2), (1, 3, 3), (4, 5, 4), (6, 8, 4)]
[(7, 9, 2), (1, 3, 3), (4, 5, 4), (5, 7, 4), (6, 8, 4), (5, 6, 5), (3, 5, 6), (2, 4, 10)]

