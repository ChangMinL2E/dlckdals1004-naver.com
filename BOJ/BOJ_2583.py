# BOJ_2583 영역 구하기
import sys
from collections import deque
input = sys.stdin.readline

N,M,point_cnt = map(int,input().split())
visited = [[0]*M for _ in range(N)]
for _ in range(point_cnt):
    st_x,st_y,ed_x,ed_y = map(int,input().split())
    for i in range(st_x,ed_x):
        for j in range(st_y,ed_y):
            visited[j][i] += 1

delta = [(0,1),(1,0),(0,-1),(-1,0)]

blanks = []
Queue=deque([])

for i in range(N):
    for j in range(M):
        if not visited[i][j]: # == 0:
            Queue.append((i,j))
            visited[i][j] = 1
            cnt = 1
            while Queue:
                q = Queue.popleft()


                for dt in delta:
                    x,y = q[0]+dt[0],q[1]+dt[1]
                    if 0<=x<N and 0<=y<M and not visited[x][y]:
                        visited[x][y] = 1
                        Queue.append((x,y))
                        cnt += 1

            blanks.append(cnt)

blanks.sort()
print(len(blanks))
print(*blanks)






