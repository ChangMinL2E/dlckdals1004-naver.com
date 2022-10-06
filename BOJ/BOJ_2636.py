# BOJ_2636 치즈

from collections import deque

rows, cols = map(int,input().split())
cheezes = [list(map(int,input().split())) for _ in range(rows)]
delta = [(0,1),(1,0),(0,-1),(-1,0)]

Queue = deque()
Lst = [] # 치즈 모음
cheezes_count = len(Lst)

for i in range(rows):
    for j in range(cols):
        if cheezes[i][j] == 1:
            Lst.append((i,j))

cnt = 0
while True:
    total = 0
    frozen = []
    for ch in Lst:
        for dt in delta:
            x,y = ch[0]+dt[0], ch[1]+dt[1]
            if 0<=x<rows and 0<=y<cols:
                if cheezes[x][y] == 0:
                    total +=1
                    Lst.remove(ch)
                    frozen.append(ch)
                    break

    if total == cheezes_count:
        print(cnt+1)
        print(total)
        break
    else:
        cnt += 1
        print(frozen)
        # for fr in frozen:
        #     Lst[fr[0]][fr[1]] = 0









