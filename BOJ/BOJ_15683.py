# BOJ_15683 감시

import sys
input = sys.stdin.readline
from collections import deque # for문으로 해도 되긴하는데, 그냥 Queue 쓰기 위해
from copy import deepcopy # 메모리 널널하게 줘서, recursion 보낼때, lst 인자로 주기위해,

def recursion(Lst2,k,N):
    global minimum

    if k == N:
        total = 0
        for ls in Lst2: # 시간초과 나오면, recursion 인자로 0 갯수 넣어서 넘겨서 재도전
            total += ls.count(0)
        if minimum > total:
            minimum = total
        return

    a,b = cctvs_where[k] # 이번에 볼 cctv 위치
    kindofcctv = Lst[a][b] # cctv 종류
    for direct in cctvs[kindofcctv]: # cctv 종류에 따라 볼 방향? 각도?
        # 낙서할 지도를 가져온다.
        lst = deepcopy(Lst2) # 감시구역 지도 복사하고, 여기에 칠해서 넘길 예정

        for dt in direct: # 번호에 따른 갈 방향(배열안에 배열안에 튜플로 만들어준 이유)

            Queue = deque([(a,b)]) # 현재 위치부터, 내가 생각한 방향으로 계속 가다가 막히면 그만,
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

# cctv 목록들인데, 방향? 각도? 별로 다 봐야하니까 배열안에 배열안에 튜플형식, 이해 안되면 디버깅 돌려보기
cctvs = [0,[[(0,1)],[(1,0)],[(0,-1)],[(-1,0)]], # 1번
         [[(0,1),(0,-1)],[(1,0),(-1,0)]], # 2번
         [[(0,1),(1,0)],[(0,-1),(1,0)],[(0,1),(-1,0)],[(0,-1),(-1,0)]], # 3번
         [[(0,1),(1,0),(0,-1)],[(0,-1),(1,0),(-1,0)],[(0,-1),(0,1),(-1,0)],[(0,1),(-1,0),(1,0)]], # 4번
         [[(0,1),(0,-1),(1,0),(-1,0)]]] # 5번

Lst = [list(map(int,input().split())) for _ in range(row)] # 지도? 감시구역?

cctvs_cnt = 0 # 재귀함수 종료조건
minimum = 1e10
cctvs_where = [] # cctv 위치 목록
for i in range(row):
    for j in range(col):
        if Lst[i][j] != 0 and Lst[i][j] != 6:
            cctvs_where.append((i,j)) # cctv 위치 목록넣기, 갯수 추가
            cctvs_cnt += 1

recursion(Lst,0,cctvs_cnt) # 첫번째 cctv부터 보겠습니다.
print(minimum)





