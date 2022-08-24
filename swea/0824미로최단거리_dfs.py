def dfs(i,j,N):
    if maze[i][j] == 3:
        return
    else:
        visited[i][j] = 1
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni,nj,N)

T = int(input())
