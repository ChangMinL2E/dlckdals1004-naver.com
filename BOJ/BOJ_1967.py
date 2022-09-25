# BOJ_1967 트리의 지름 / 가중치

N = int(input())
Tree = [[(0,0),(0,0)] for _ in range(N+1)]
visited = [False]*(N+1)
Parent = [(0,0)]*(N+1)
maximum = 0

for _ in range(N-1):
    par,child,weight = map(int,input().split())
    if Tree[par][0] == 0:
        Tree[par][0] = (child,weight)
    else:
        Tree[par][1] = (child,weight)
    Parent[child] = (par, weight)


def w_l(idx,total):
    global maximum

    if idx == 0:
        if total > maximum:
            maximum = total
        return

    if not visited[idx]:
        visited[idx] = True
        child1, weight1, child2, weight2 = Tree[idx][0][0], Tree[idx][0][1], Tree[idx][1][0], Tree[idx][1][1]

        w_l(child1,total+weight1)
        w_l(child2,total+weight2)
        visited[idx] = False


def parent(idx, total):
    if idx and not visited[idx]:
        visited[idx] = True
        parent(Parent[idx][0],total+Parent[idx][1])
        child1, weight1, child2, weight2 = Tree[idx][0][0], Tree[idx][0][1], Tree[idx][1][0], Tree[idx][1][1]

        w_l(child1, total + weight1)
        w_l(child2, total + weight2)
        visited[idx] = False


for i in range(2,N+1):
    if Tree[i] == [(0,0),(0,0)]:
        # visited[i] = True
        parent(i,0)


print(maximum)
