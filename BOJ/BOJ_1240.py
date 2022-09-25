# BOJ_1240 노드 사이의 거리

N, M = map(int,input().split())
dic = {}
for i in range(1001):
    dic[i] = []

visited = [False]*(1001)


for _ in range(N-1):
    node1, node2, distance = map(int,input().split())
    dic[node1].append((node2, distance))
    dic[node2].append((node1, distance))

def dfs(idx, end, total):
    if idx == end:
        print(total)
        return

    if not visited[idx]:
        for lst in dic[idx]:
            node, distance2 = lst[0], lst[1]
            visited[idx] = True
            dfs(node, end, total+distance2)
            visited[idx] = False

for _ in range(M):
    st, ed = map(int,input().split())
    dfs(st,ed,0)



