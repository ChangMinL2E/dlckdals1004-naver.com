# BOJ_11724 연결 요소의 개수 / BFS

from collections import deque
N, M = map(int,input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

# print(edges)
visited = [False]*(N+1)

Queue = deque([x for x in range(1,N+1)])
# print(Queue)

total = 0
while Queue:
    q = Queue.popleft()
    # 아예 처음?
    if not visited[q]:
        # 한덩이 추가
        total += 1
        # 연결된거 다 보겠다.
        Queue2 = deque()
        for ele in edges[q]:
            Queue2.append(ele)
        while Queue2:
            q2 = Queue2.popleft()
            if not visited[q2]:
                visited[q2] = True
                for ele2 in edges[q2]:
                    Queue2.append(ele2)

print(total)






