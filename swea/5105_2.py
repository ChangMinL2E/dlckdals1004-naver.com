# 5105. 미로의 거리

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = []
    maze.append([1]*(N+2))
    for _ in range(N):
        maze.append([1]+list(map(int, input()))+[1])
    maze.append([1]*(N+2))

    queue = []
    visited = [[0] * (N+2) for _ in range(N+2)]


    for i in range(N+2):
        for j in range(N+2):
            if maze[i][j] == 2:
                st = (i, j)
            elif maze[i][j] == 3:
                ed = (i, j)

    queue.append(st)
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[st[0]][st[1]] = 1

    cml = True
    while cml:
        shot = queue.pop(0)
        x, y = shot[0], shot[1]

        for new in delta:
            dx, dy = new[0], new[1]
            if maze[x + dx][y + dy] == 0 and visited[x + dx][y + dy] == 0:
                visited[x + dx][y + dy] = visited[x][y] + 1
                queue.append((x + dx, y + dy))

            elif maze[x + dx][y + dy] == 3:
                visited[x + dx][y+dy] = visited[x][y] + 1
                cml = False
        if not queue:
            cml = False

    if visited[ed[0]][ed[1]] != 0:
        print(f'#{tc} {visited[ed[0]][ed[1]]-2}')
    else:
        print(f'#{tc} 0')