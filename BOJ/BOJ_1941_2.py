# BOJ_1941 소문난 칠공주

def per(lst,k,N,curSum):
    if curSum + (N-k) < 4:
        return

    if k == N:
        lst.sort()
        if not lst in Lst:
            Lst.append(lst)
        return

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                for dt in delta: # 상,하,위,아래 로 닿아있다면,
                    x,y = i+dt[0],j+dt[1]
                    if 0<=x<5 and 0<=y<5 and visited[x][y]:
                        visited[i][j] = True
                        lst.append((i,j))
                        if Girls[i][j] == 'Y':
                            per(lst,k+1,N,curSum)
                        else:
                            per(lst,k+1,N,curSum+1)
                        lst.pop()
                        visited[i][j] = False
                        break
                else:
                    return

Girls = [list(input()) for _ in range(5)]
delta = [(0,1),(0,-1),(1,0),(-1,0)]
visited = [[False]*5 for _ in range(5)]
Lst = []

for i in range(5):
    for j in range(5):
        if Girls[i][j] == 'S':
            visited[i][j] = True
            per([(i,j)],1,7,1)
            visited[i][j] = False

print(Lst)



