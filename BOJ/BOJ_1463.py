# BOJ_1463 1로 만들기

from collections import  deque
visited = [0]*1000001

N = int(input())
Queue = deque([N])

while Queue:
    q = Queue.popleft()
    if q == 1:
        print(visited[q])
        break

    if not q%2 and not visited[q//2]:
        visited[q//2] = visited[q]+1
        Queue.append(q//2)
    if not q%3 and not visited[q//3]:
        visited[q//3] = visited[q]+1
        Queue.append(q // 3)
    if not visited[q-1]:
        visited[q-1] = visited[q]+1
        Queue.append(q -1)





