# 02 완전 검색 최소합 문제

def Backtracking(lst,x,y,curSum):
    global minimum

    if curSum > minimum:
        return

    if x==N-1 and y==N-1:
        if curSum < minimum:
            minimum = curSum
        return

    for dt in delta:
        x1 = x + dt[0] # 갈 수 있는 방향
        y1 = y + dt[1]
        if 0 <= x1 <= N-1 and 0 <= y1 <= N-1 and not visited[x1][y1]:
            visited[x1][y1] = True
            Backtracking(lst,x1,y1,curSum+lst[x1][y1])
            visited[x1][y1] = False

# delta = [(-1,0),(1,0),(0,-1),(0,1)] 왜 배제?
delta = [(1,0),(0,1)]

for tc in range(1,int(input())+1):
    N = int(input())
    minimum = 100000000
    visited = [[False for _ in range(N)] for _ in range(N)]

    Matrix = []
    for _ in range(N):
        Matrix.append(list(map(int,input().split())))

    Backtracking(Matrix,0,0,Matrix[0][0])

    print(f'#{tc} {minimum}')





