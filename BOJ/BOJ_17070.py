# BOJ_17070 파이프 옮기기 1

def per(x,y,N,direction):
    global total
    if x==N-1 and y == N-1:
        total += 1
        return

    if direction == 1:
        if 0<=x<N and 0<=y+1<N and not Lst[x][y+1]: # 방향 그대로 ->
            per(x,y+1,N,1)
        if 0<=x+1<N and 0<=y+1<N and (not Lst[x+1][y+1] and not Lst[x][y+1] and not Lst[x+1][y]): # 방향 대각선
            per(x+1,y+1,N,2)
    elif direction == 2: # 대각
        if 0<=x<N and 0<=y+1<N and not Lst[x][y+1]: # 방향 그대로 ->
            per(x,y+1,N,1)
        if 0<=x+1<N and 0<=y+1<N and (not Lst[x+1][y+1] and not Lst[x][y+1] and not Lst[x+1][y]): # 방향 대각선
            per(x+1,y+1,N,2)
        if 0<=x+1<N and 0<=y<N and not Lst[x+1][y]: # 방향 아래
            per(x+1,y,N,3)
    else: # 아래
        if 0<=x+1<N and 0<=y+1<N and (not Lst[x+1][y+1] and not Lst[x][y+1] and not Lst[x+1][y]): # 방향 대각선
            per(x+1,y+1,N,2)
        if 0<=x+1<N and 0<=y<N and not Lst[x+1][y]: # 방향 아래
            per(x+1,y,N,3)




N = int(input())
Lst = [list(map(int,input().split())) for _ in range(N)]
total = 0
direct = {
    1: (0,1),
    2: (1,1),
    3: (1,0)
}

per(0,1,N,1)

print(total)





