# BOJ_10026 BFS 적록색약

import sys
from collections import deque
import copy

N = int(sys.stdin.readline())
cnt1 = 1 # 정상인
cnt2 = 1 # 적록색약
lst = []
for _ in range(N):
    lst.append(list(sys.stdin.readline().strip())) # 공백 제거를 위해 strip()

RG_lst = [[] for _ in range(N)] # 적록색약 리스트

for idx in range(len(lst)): # 적록색약 처리
    for ele in lst[idx]:
        RG_lst[idx].append(ele.replace('R','G'))

# 정상인 R/G/B
visited1 = [[False for _ in range(N)] for _ in range(N)]
# 적록색약 인 사람 R-G/B
visited2 = [[False for _ in range(N)] for _ in range(N)]

Queue1 = deque()
Queue2 = deque()

Queue1.append((0,0))
Queue2.append((0,0))
visited1[0][0] = True
visited2[0][0] = True
delta = [(0,1),(0,-1),(1,0),(-1,0)]


# 정상인
for x in range(N):
    for y in range(N):
        if (x,y) in Queue1:
            while Queue1:
                point = Queue1.popleft()
                for dt in delta:
                    x1,y1 = point[0]+dt[0], point[1]+dt[1]
                    if 0<=x1<=N-1 and 0<=y1<=N-1 and not visited1[x1][y1] and lst[point[0]][point[1]] == lst[x1][y1]:
                        Queue1.append((x1,y1))
                        visited1[x1][y1] = True
        else: # 새로운 영역이면,
            if not visited1[x][y]:
                cnt1 += 1
                Queue1.append((x,y))
                visited1[x][y] = True
                while Queue1:
                    point = Queue1.popleft()
                    for dt in delta:
                        x1, y1 = point[0] + dt[0], point[1] + dt[1]
                        if 0 <= x1 <= N - 1 and 0 <= y1 <= N - 1 and not visited1[x1][y1] and lst[point[0]][point[1]] == lst[x1][y1]:
                            Queue1.append((x1, y1))
                            visited1[x1][y1] = True

# 색록적약
for x in range(N):
    for y in range(N):
        if (x,y) in Queue2:
            while Queue2:
                point = Queue2.popleft()
                for dt in delta:
                    x1,y1 = point[0]+dt[0], point[1]+dt[1]
                    if 0<=x1<=N-1 and 0<=y1<=N-1 and not visited2[x1][y1] and RG_lst[point[0]][point[1]] == RG_lst[x1][y1]:
                            Queue2.append((x1,y1))
                            visited2[x1][y1] = True

        else: # 새로운 영역이면,
            if not visited2[x][y]:
                cnt2 += 1
                Queue2.append((x,y))
                visited2[x][y] = True
                while Queue2:
                    point = Queue2.popleft()
                    for dt in delta:
                        x1, y1 = point[0] + dt[0], point[1] + dt[1]
                        if 0 <= x1 <= N - 1 and 0 <= y1 <= N - 1 and not visited2[x1][y1] and RG_lst[point[0]][
                            point[1]] == RG_lst[x1][y1]:
                            Queue2.append((x1, y1))
                            visited2[x1][y1] = True


print(cnt1, cnt2)










