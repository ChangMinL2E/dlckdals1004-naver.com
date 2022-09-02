# BOJ_1926 그림
# 다시 풀자.


row, col= map(int,input().split())

Matrix = []
for _ in range(row):
    Matrix.append(list(map(int,input().split())))


delta = [(-1,0),(1,0),(0,-1),(0,1)]
cnt = 0
Queue = []
maximum = 0

for i in range(row):
    for j in range(col):
        if Matrix[i][j] == 1:
            cnt += 1
            Queue.append((i,j))
            Matrix[i][j] = 0
            width = 0
            while Queue:
                a,b = Queue.pop(0)
                width += 1
                for dt in delta:
                    if 0<=a+dt[0]<row and 0<= b+dt[1] < col and Matrix[a+dt[0]][b+dt[1]]:
                        Queue.append((a+dt[0],b+dt[1]))
                        Matrix[a+dt[0]][b+dt[1]] = 0
            
            if width > maximum:
                maximum = width
                    
print(cnt)
print(width)




