# BOJ_1260 DFS와 BFS

from collections import deque
N, M, V = map(int,input().split())

visited = [False]*(N+1)
lst = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

for ls in lst:
    ls.sort()

Go_dfs = [V]
Go_bfs = [V]
visited[V] = True
Queue = deque()
Queue.append(V)

while Queue:
    q = Queue.popleft()
    for point in lst[q]:
        if not visited[point]:
            Queue.append(point)
            Go_bfs.append(point)
            visited[point] = True



visited = [False]*(N+1)
visited[V] = True
Stack = deque()
Stack.append(V)


while Stack:
    s = Stack[-1]
    cnt = 0
    for point in lst[s]:
        if not visited[point]:
            Stack.append(point)
            Go_dfs.append(point)
            visited[point] = True
            cnt += 1
            break
    if cnt == 0:
        Stack.pop()


print(*Go_dfs)
print(*Go_bfs)