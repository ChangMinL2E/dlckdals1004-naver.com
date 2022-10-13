# BOJ_16953 A->B / BFS

from collections import deque

A,B = map(int,input().split())
visited = [-1]*(1000000000+1)

visited[A] = 1
Queue = deque([A])
result = -1
while Queue:
    q = Queue.popleft()
    if q == B:
        break

    if 2*q <= B and visited[2*q] == -1:
        visited[2*q] = visited[q]+1
        Queue.append(2*q)
    if 10*q+1 <= B and visited[10*q+1]:
        visited[10*q+1] = visited[q]+1
        Queue.append(10*q+1)
print(visited[B])






