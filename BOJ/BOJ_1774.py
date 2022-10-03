# BOJ_1774 우주신과의 교감 / MST

def distance(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**(1/2)

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    rep[find_set(y)] = find_set(x)

V, current_E = map(int,input().split())
points = [list(map(int,input().split())) for _ in range(V)]
rep = [x for x in range(V+1)]

edge = []
for i in range(V-1):
    for j in range(i+1,V):
        edge.append((i+1,j+1,distance(points[i],points[j])))

# print(edge)
for _ in range(current_E):
    st, ed = map(int,input().split())
    Union(find_set(st), find_set(ed))

edge.sort(key= lambda x:x[2])
cnt = current_E
total = 0

if cnt != V-1:
    for a, b, weight in edge:

        if find_set(a) != find_set(b):
            cnt += 1
            total += weight
            Union(a,b)

        if cnt == V-1:
            break

print("{:.2f}".format(total))
# print(round(total,2))

# print(edge)






