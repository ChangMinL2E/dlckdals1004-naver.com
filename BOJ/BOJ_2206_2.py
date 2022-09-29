# BOJ_2206 벽 부수고 이동하기 BFS

import sys
from collections import deque

rows, cols = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().strip())) for _ in range(rows)]
visited = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(2)]
visited[1][0][0] = 1
# chance = 1
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
Queue = deque()
Queue.append((0,0,1))
sol = -1
while Queue:
    q = Queue.popleft()
    if q[0] == rows-1 and q[1] == cols-1:
        sol = visited[q[2]][-1][-1]
        break
    # 길이 뚫린것부터!
    for dt in delta:
        x, y, z = q[0] + dt[0], q[1] + dt[1], q[2]
        if 0 <= x < rows and 0 <= y < cols and lst[x][y] == 0 and visited[z][x][y] == 0:
            visited[z][x][y] = visited[z][q[0]][q[1]]+1
            Queue.append((x,y,z))
        # 길 막힌 경우도 전부 뚫어보자!
        elif q[2] == 1 and 0 <= x < rows and 0 <= y < cols and lst[x][y] == 1 and visited[0][x][y] == 0:
            visited[0][x][y] = visited[z][q[0]][q[1]]+1
            Queue.append((x, y, 0))

if sol == -1:
    print(-1)
else:
    print(sol)
