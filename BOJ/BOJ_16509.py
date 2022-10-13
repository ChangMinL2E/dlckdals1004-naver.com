# BOJ_16509 장군 / Backtracking

def Backtracking(ele,K,cnt):
    global minimum

    if cnt > minimum:
        return

    if ele[0]==K[0] and ele[1]==K[1]:
        minimum = cnt
        return

    for idx in range(len(delta)):
        x,y = ele[0]+delta[idx][0],ele[1]+delta[idx][1]
        if 0<=x<10 and 0<=y<9 and not visited[x][y]:
            if king != (ele[0]+Go[idx][0][0],ele[1]+Go[idx][0][1]) and king != (ele[0]+Go[idx][1][0],ele[1]+Go[idx][1][1]):
                visited[x][y] = True
                Backtracking((x,y),K,cnt+1)
                visited[x][y] = False

minimum = 1e10
Go = [[(1,0),(2,1)],[(1,0),[2,-1]],[(-1,0),(-2,1)],[(-1,0),(-2,-1)],[(0,1),(1,2)],[(0,-1),(1,-2)],[(0,1),(-1,2)],[(0,-1),(-1,-2)]]
delta = [(3,2),(3,-2),(-3,2),(-3,-2),(2,3),(2,-3),(-2,3),(-2,-3)]
elephant = tuple(map(int,input().split()))
king = tuple(map(int,input().split()))
visited = [[False]*9 for _ in range(10)]

visited[elephant[0]][elephant[1]] = True
Backtracking(elephant,king,0)

if minimum != 1e10:
    print(minimum)
else:
    print(-1)