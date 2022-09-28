# BOJ_5014 스타트링크
from collections import deque

F, S, G, U, D = map(int,input().split())

visited = [0]*(F+1)
Queue = deque()
Queue.append(S)
visited[S] = 1

while Queue:
    q = Queue.popleft()
    if q == G:
        Queue = deque()
        break

    if 0 < q+U <= F and not visited[q+U]:
        Queue.append(q+U)
        visited[q+U] = visited[q]+1

    if 0 < q-D <= F and not visited[q-D]:
        Queue.append(q-D)
        visited[q-D] = visited[q]+1

if visited[G]:
    print(visited[G]-1)
else:
    print("use the stairs")







