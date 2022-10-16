# BOJ_16953 A->B / BFS

from collections import deque

A,B = map(int,input().split())
# visited = [-1]*(B+1)

# visited[A] = 1
Queue = deque([(A,1)])
result = -1
while Queue:
    q = Queue.popleft()
    if q[0] == B:
        result = q[1]
        break

    if 2*q[0] <= B:# and visited[2*q] == -1:
        #visited[2*q] = visited[q]+1
        Queue.append((2*q[0],q[1]+1))
    if 10*q[0]+1 <= B: # and visited[10*q+1] == -1:
        #visited[10*q+1] = visited[q]+1
        Queue.append((10*q[0]+1,q[1]+1))
print(result)






