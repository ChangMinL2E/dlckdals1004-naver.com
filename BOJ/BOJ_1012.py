# BOJ_1012.py 유기농 배추

for _ in range(int(input())):
    col, row, N = map(int,input().split())

    Matrix = [[0 for _ in range(col)] for _ in range(row)]
    for _ in range(N):
        y, x = map(int,input().split())
        Matrix[x][y] = 1

    delta = [(-1,0),(1,0),(0,-1),(0,1)]
    cnt = 0
    Queue = []
    available = []

    for i in range(row):
        for j in range(col):
            if Matrix[i][j] == 1:
                cnt += 1
                Queue.append((i,j))
                Matrix[i][j] = 0
                while Queue:
                    a,b = Queue.pop(0)
                    for dt in delta:
                        if 0<=a+dt[0]<row and 0<= b+dt[1] < col and Matrix[a+dt[0]][b+dt[1]]:
                            Queue.append((a+dt[0],b+dt[1]))
                            Matrix[a+dt[0]][b+dt[1]] = 0
                        
    print(cnt)
                    









