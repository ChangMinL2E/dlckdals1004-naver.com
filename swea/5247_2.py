# swea 5247 - 연산

from collections import deque

for tc in range(1,int(input())+1):
    st, ed = map(int,input().split())
    visited = [-1]*1000001
    Queue = deque()
    Queue.append(st)
    visited[st] = 0
    while Queue:
        q = Queue.popleft()
        if q == ed:
            Queue = []
            break

        for Q in [q+1, q-1, q*2, q-10]:
            if 0<=Q<=1000000 and visited[Q] == -1:
                visited[Q] = visited[q] + 1
                Queue.append(Q)

    print(f'#{tc} {visited[ed]}')




