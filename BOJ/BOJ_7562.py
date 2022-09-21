# BOJ_7562 나이트

import sys
from collections import deque

delta = [(2,-1),(2,1),(-2,1),(-2,-1),(1,-2),(1,2),(-1,-2),(-1,2)]

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    x,y = map(int,sys.stdin.readline().split())
    a,b = map(int,sys.stdin.readline().split())
    visited = [[0 for _ in range(N)] for _ in range(N)]

    Queue = deque()
    Queue.append((x,y))
    while Queue:
        night = Queue.popleft()
        if night == (a,b):
            print(visited[a][b])
            break

        for dt in delta:
            x1, y1 = night[0]+dt[0],night[1]+dt[1]
            if 0<=x1<N and 0<=y1<N and not visited[x1][y1]:
                Queue.append((x1,y1))
                visited[x1][y1] = visited[night[0]][night[1]] + 1



