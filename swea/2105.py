# swea 2105 Dessert Cafe / Backtracking

def Backtracking(lst, which, cnt):
    global Desserts, maximum


    if len(which) >= 2 and which[-1] == which[0]:
        if len(which)-1 > maximum:
            maximum = len(which)-1
        return

    if lst.count(lst[-1]) >= 2:
        return

    x_now, y_now = which[-1][0], which[-1][1]
    for i in [0,1]:
        cnt += i
        if cnt<5:
        # x,y = which[-1][0]+delta[cnt%4][0], which[-1][1]+delta[cnt%4][1]
            x,y = x_now+delta[cnt%4][0], y_now+delta[cnt%4][1]
            if 0<= x < N and 0<= y < N:
                lst.append(Desserts[x][y])
                which.append((x,y))
                Backtracking(lst, which, cnt)
                lst.pop()
                which.pop()



for tc in range(1, int(input()) + 1):
    N = int(input())
    maximum = -1
    Desserts = [list(map(int, input().split())) for _ in range(N)]
    # total_lst = []
    delta = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


    for i in range(N):
        for j in range(N):
            if not (i,j) in [(0,0),(N-1,0),(0,N-1),(N-1,N-1)]:
                Backtracking([Desserts[i][j]],[(i,j)],0)
            # print(i,j)
            # print(maximum)

    print(f'#{tc} {maximum}')


