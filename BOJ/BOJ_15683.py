# BOJ_15683 감시

import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

def recursion(Lst2,k,N):
    global minimum

    if k == N:
        total = 0
        for ls in Lst2:
            total += ls.count(0)
        if minimum > total:
            minimum = total
        return

    a,b = cctvs_where[k]
    kindofcctv = Lst[a][b]
    for direct in cctvs[kindofcctv]:
        # 낙서할 지도를 가져온다.
        lst = deepcopy(Lst2)

        for dt in direct: # 번호에 따른 갈 방향

            Queue = deque([(a,b)])
            while Queue:
                q = Queue.popleft()
                x,y = q[0]+dt[0], q[1]+dt[1]
                if 0<=x<row and 0<=y<col:
                    if lst[x][y] == 0:
                        lst[x][y] = '#'
                        Queue.append((x,y))
                    elif lst[x][y] == 6:
                        break
                    else:
                        Queue.append((x,y))
                else:
                    break

        recursion(lst,k+1,N)


row, col = map(int,input().split())

cctvs = [0,[[(0,1)],[(1,0)],[(0,-1)],[(-1,0)]], # 1번
         [[(0,1),(0,-1)],[(1,0),(-1,0)]], # 2번
         [[(0,1),(1,0)],[(0,-1),(1,0)],[(0,1),(-1,0)],[(0,-1),(-1,0)]], # 3번
         [[(0,1),(1,0),(0,-1)],[(0,-1),(1,0),(-1,0)],[(0,-1),(0,1),(-1,0)],[(0,1),(-1,0),(1,0)]], # 4번
         [[(0,1),(0,-1),(1,0),(-1,0)]]] # 5번

Lst = [list(map(int,input().split())) for _ in range(row)]

cctvs_cnt = 0
minimum = 1e10
cctvs_where = []
for i in range(row):
    for j in range(col):
        if Lst[i][j] != 0 and Lst[i][j] != 6:
            cctvs_where.append((i,j))
            cctvs_cnt += 1

recursion(Lst,0,cctvs_cnt)
print(minimum)





