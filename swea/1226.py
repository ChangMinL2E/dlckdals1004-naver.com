# 1226. 미로

for tc in range(1,11):
    input()
    visited = [[0] * 16 for _ in range(16)]
    queue = []
    maze = []
    for _ in range(16):
        N = list(map(int, input()))
        maze.append(N)

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                st = (i, j)
            elif maze[i][j] == 3:
                ed = (i, j)

    visited[st[0]][st[1]] = 1
    queue.append(st)

    news = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        front = queue.pop(0)
        for new in news:
            dx, dy = new[0], new[1]
            x, y = front[0], front[1]
            if visited[x+dx][y+dy] == 0 and maze[x+dx][y+dy] != 1:
                queue.append((x + dx, y + dy))
                visited[x + dx][y + dy] = 1

    if visited[ed[0]][ed[1]] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
