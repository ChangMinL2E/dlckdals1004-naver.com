# BOJ_2206 벽 부수고 이동하기 BFS

import sys


def BFS(lst, which, chance):
    global minimum

    if which == (rows - 1, cols - 1):
        if minimum > visited[rows - 1][cols - 1]:
            minimum = visited[rows - 1][cols - 1]
        return

    if visited[which[0]][which[1]] > minimum:
        return

    x_now, y_now = which[0], which[1]

    # 길이 뚫린것부터!
    for dt in delta:
        x, y = x_now + dt[0], y_now + dt[1]
        if 0 <= x < rows and 0 <= y < cols and visited[x][y] == 0 and lst[x][y] == 0:
            visited[x][y] = visited[x_now][y_now] + 1
            BFS(lst, (x, y), chance)
            visited[x][y] = 0

    # 길 막힌 경우도 전부 뚫어보자!
    if chance == 1:
        for dt in delta:
            x, y = x_now + dt[0], y_now + dt[1]
            if 0 <= x < rows and 0 <= y < cols and visited[x][y] == 0 and lst[x][y] == 1:
                visited[x][y] = visited[x_now][y_now] + 1
                BFS(lst, (x, y), 0)
                visited[x][y] = 0


minimum = 100000000
rows, cols = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().strip())) for _ in range(rows)]
visited = [[0 for _ in range(cols)] for _ in range(rows)]
visited[0][0] = 1
# chance = 1
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
BFS(lst, (0,0), 1)

if minimum == 100000000:
    minimum = -1
print(minimum)