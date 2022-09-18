# 1861. 정사각형 방

def Backtracking(lst, cnt, x, y,start_x,start_y):
    global maximum

    if cnt >= maximum:
        maximum = cnt
        start.append((start_x,start_y, cnt))

    for dt in delta:
        if 0<=x+dt[0]<=N-1 and 0<=y+dt[1]<=N-1 and not visited[x+dt[0]][y+dt[1]] and lst[x+dt[0]][y+dt[1]] == lst[x][y] + 1:
            visited[x+dt[0]][y+dt[1]] = True
            Backtracking(lst, cnt+1, x+dt[0], y+dt[1],start_x,start_y)
            visited[x+dt[0]][y+dt[1]] = False


delta = [(0,1),(1,0),(0,-1),(-1,0)]

for tc in range(1,int(input())+1):
    N = int(input())
    maximum = 0

    start = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    Rooms = []
    for _ in range(N):
        Rooms.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(N):
            visited[i][j] = True
            Backtracking(Rooms, 1, i, j, i,j)
            visited[i][j] = False

    start = sorted(start, key=lambda x: x[2], reverse = True)
    start = [st for st in start if st[2] == maximum]
    real_start = 100000000
    for st in start:
        if Rooms[st[0]][st[1]] < real_start:
            real_start = Rooms[st[0]][st[1]]

    print(f'#{tc} {real_start} {maximum}')

