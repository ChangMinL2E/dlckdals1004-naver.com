# BOJ_7569 토마토 BFS
from collections import deque

N,M,H =map(int,input().split())
BOX = [[list(map(int,input().split())) for _ in range(M)] for _ in range(H)]

visited = [[[0 for _ in range(N)] for _ in range(M)] for _ in range(H)]
delta = [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]
cnt = 0

Queue = deque()
for i in range(M):
    for j in range(N):
        for k in range(H):
            if BOX[k][i][j] == 1:
                Queue.append((i,j,k))
                cnt += 1
            elif BOX[k][i][j] == -1:
                visited[k][i][j] = -1
                cnt += 1

maximum = 0
while Queue:
    st = Queue.popleft()
    for dt in delta:
        x,y,z = st[0]+dt[0], st[1]+dt[1], st[2]+dt[2]
        if 0<=x<M and 0<=y<N and 0<=z<H and BOX[z][x][y]==0 and visited[z][x][y] == 0:
            Queue.append((x,y,z))
            visited[z][x][y] = visited[st[2]][st[0]][st[1]] + 1
            if maximum < visited[z][x][y]:
                maximum = visited[z][x][y]
            cnt += 1

if cnt != N*M*H:
    maximum = -1

print(maximum)



