# BOJ_14938 서강그라운드
# 갈 수 있는 지역을 전부 찾고 난 후에, total을 구해야겠다.
from collections import deque

def recursion(Queue): # Queue (현재위치, 거리)
    global total_maximum
    visited = [False] * (n + 1)

    total = 0
    while Queue:
        q = Queue.popleft()
        visited[q[0]] = True
        # total += items[q[0]]
        for idx in range(n+1):
            if G[q[0]][idx] and m >= q[1] + G[q[0]][idx]:# and not visited[idx]:
                Queue.append((idx, q[1]+G[q[0]][idx]))
    for idx in range(n+1):
        if visited[idx]:
            total += items[idx]

    if total_maximum < total:
        total_maximum = total

    return

total_maximum = 0
n,m,r = map(int,input().split())
items = [0]
items.extend(list(map(int,input().split())))
G = [[0]*(n+1) for _ in range(n+1)]
# print(items)

for _ in range(r):
    a,b,dis = map(int,input().split())
    G[a][b] = dis
    G[b][a] = dis

# print(G)
for i in range(1,n+1):
    recursion(deque([(i,0)]))

print(total_maximum)





