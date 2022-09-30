# 1249 보급로
from collections import deque

for tc in range(1,int(input())+1):
    N = int(input())
    Lst = [list(map(int,input())) for _ in range(N)]
    visited = [[1e10]*N for _ in range(N)]
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    Queue = deque()
    Queue.append((0,0))
    visited[0][0] = 0

    while Queue:
        q = Queue.popleft()
        # if q[0]==N-1 and q[1] == N-1:
        #     break

        for dt in delta:
            x,y = q[0]+dt[0],q[1]+dt[1]
            if 0<=x<N and 0<=y<N and visited[x][y] > visited[q[0]][q[1]]+Lst[x][y]:
                Queue.append((x,y))
                visited[x][y] = visited[q[0]][q[1]]+Lst[x][y]

    print(f'#{tc} {visited[-1][-1]}')




