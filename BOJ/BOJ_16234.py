# BOJ_16234 인구 이동
from collections import deque

N, L, R = map(int,input().split())

Lst = [list(map(int,input().split())) for _ in range(N)]
# visited = [[False]*N for _ in range(N)]
delta = [(1,0),(-1,0),(0,1),(0,-1)]
total_cnt = 0
cml = True
while cml:
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                cnt = 0
                # if not visited[i][j]:
                Queue = deque()
                countrys = deque()
                total = Lst[i][j]
                # cnt = 0
                Queue.append((i,j))
                countrys.append((i,j))
                while Queue:
                    q = Queue.popleft()
                    # visited[q[0]][q[1]] = True
                    for dt in delta:
                        x,y = q[0]+dt[0], q[1]+dt[1]
                        if 0<=x<N and 0<=y<N and L <= abs(Lst[q[0]][q[1]] - Lst[x][y]) <= R and not (x,y) in countrys and not visited[x][y]:
                            Queue.append((x,y))
                            visited[x][y] = True
                            cnt += 1
                            countrys.append((x,y))
                            total += Lst[x][y]
                if cnt != 0:
                    for country_x, country_y in countrys:
                        Lst[country_x][country_y] = total//(cnt+1)

                # if cnt:
                    count += 1
    if not count:
        cml = False
    else:
        total_cnt += 1

print(total_cnt)









