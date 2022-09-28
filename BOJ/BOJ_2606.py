# BOJ_2606 바이러스 / BFS
from collections import deque

N = int(input())
lst = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

visited = [False]*(N+1)
Queue = deque()
Queue.append(1)
visited[1] = True

while Queue:
    q = Queue.popleft()
    for point in lst[q]:
        if not visited[point]:
            visited[point] = True
            Queue.append(point)

print(visited.count(True) -1)












