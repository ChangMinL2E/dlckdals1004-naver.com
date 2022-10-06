# BOJ_2667 단지수 구하기 / BFS
from collections import  deque

N = int(input())
Lst = [list(map(int,input())) for _ in range(N)]

delta = [(0,1),(0,-1),(1,0),(-1,0)]
Queue = deque()
total = 0
total_lst = []

for i in range(N):
    for j in range(N):
        if Lst[i][j]:
            cnt = 0
            Queue.append((i,j))
            Lst[i][j] = 0
            total += 1
            while Queue:
                q = Queue.popleft()
                cnt += 1
                for dt in delta:
                    x,y = dt[0]+q[0],dt[1]+q[1]
                    if 0<=x<N and 0<=y<N and Lst[x][y]:
                        Lst[x][y] = 0
                        Queue.append((x,y))
            total_lst.append(cnt)

print(total)
total_lst.sort()
for ls in total_lst:
    print(ls)

