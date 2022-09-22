# BOJ_5427 BFS 불
from collections import deque
import sys

for _ in range(int(sys.stdin.readline())):
    cols, rows = map(int, sys.stdin.readline().split())
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    result = "Impossible"
    Queue = deque()
    Queue.append(0)
    lst = [list(sys.stdin.readline().strip()) for _ in range(rows)]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '@':
                Queue[0] = ('@', i, j)
                visited[i][j] = 1
            elif lst[i][j] == '*':
                Queue.append(('*', i, j))
                visited[i][j] = 1
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    button = 0
    result = "IMPOSSIBLE"
    while Queue:
        point = Queue.popleft()
        if point[0] == '@' and ((point[1] == 0 or point[1] == rows - 1) or (point[2] == 0 or point[2] == cols - 1)):
            result = visited[point[1]][point[2]]
            break

        who, x_now, y_now = point[0], point[1], point[2]
        if who == '@':
            for dt in delta:
                x, y = x_now + dt[0], y_now + dt[1]
                if 0 <= x < rows and 0 <= y < cols and lst[x][y] == '.' and visited[x][y] == 0:
                    Queue.append(('@', x, y))
                    visited[x][y] = visited[x_now][y_now] + 1
                    lst[x][y] = '@'

        elif who == '*':
            for dt in delta:
                x, y = x_now + dt[0], y_now + dt[1]
                if 0 <= x < rows and 0 <= y < cols and (lst[x][y] == '.' or lst[x][y] == '@'):
                    Queue.append(('*', x, y))
                    visited[x][y] = visited[x_now][y_now] + 1
                    lst[x][y] = '*'
                    # for q in Queue:
                    #     if q[1] == x and q[2] == y and q[0] == '@':
                    #         Queue.remove(('@',x,y))

    print(result)
