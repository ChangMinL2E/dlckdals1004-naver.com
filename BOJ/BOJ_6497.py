# BOJ_6497 전력난


def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)] = find_set(x)

while True:
    V, E = map(int,input().split())
    if V == 0 and E == 0:
        break
    edges = []
    edge_total = 0
    rep = [x for x in range(V)]
    for _ in range(E):
        st,ed,weight = map(int,input().split())
        edge_total += weight
        edges.append((st,ed,weight))

    edges.sort(key=lambda x:x[2])

    cnt = 0
    total = 0
    for st,ed,weight in edges:
        if find_set(st) != find_set(ed):
            cnt += 1
            total += weight
            Union(st,ed)

        if cnt == V-1:
            break

    print(edge_total-total)