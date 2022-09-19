# BOJ_7576 토마토 BFS
from collections import deque

N,M=map(int,input().split())
BOX = [list(map(int,input().split())) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
delta = [(0,1),(0,-1),(1,0),(-1,0)]
cnt = 0

Queue = deque()
for i in range(M):
    for j in range(N):
        if BOX[i][j] == 1:
            Queue.append((i,j))
            cnt += 1
        elif BOX[i][j] == -1:
            visited[i][j] = -1
            cnt += 1

maximum = 0
while Queue:
    st = Queue.popleft()
    for dt in delta:
        x,y = st[0]+dt[0], st[1]+dt[1]
        if 0<=x<M and 0<=y<N and BOX[x][y]==0 and visited[x][y] == 0:
            Queue.append((x,y))
            visited[x][y] = visited[st[0]][st[1]] + 1
            if maximum < visited[x][y]:
                maximum = visited[x][y]
            cnt += 1
            # BOX[x][y] = 1

if cnt != N*M:
    maximum = -1
# for idx in range(M):
#     if BOX[idx].count(0) != 0:
#         maximum = -1
#     else:
#         if maximum < max(visited[idx]):
#             maximum = max(visited[idx])

print(maximum)



