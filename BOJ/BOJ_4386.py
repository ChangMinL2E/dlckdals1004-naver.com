# BOJ_4386 별자리 만들기 / MST

def distance(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**(1/2)

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)] = find_set(x)

n = int(input())
point = [list(map(float,input().split())) for _ in range(n)]
# print(point)
edge = []
for i in range(n-1):
    for j in range(i+1,n):
        edge.append((i,j,distance(point[i],point[j])))

edge.sort(key=lambda x: x[2])
rep = [x for x in range(n)]

cnt = 0
total = 0

for st,ed,dis in edge:
    if find_set(st) != find_set(ed):
        cnt += 1
        total += dis
        Union(st, ed)

    if cnt == n-1:
        break

print(round(total,2))



