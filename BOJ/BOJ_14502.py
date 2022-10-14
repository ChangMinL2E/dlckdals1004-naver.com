# BOJ_14502  

from itertools import combinations
from collections import deque
import copy

N, M = map(int,input().split())
Lst = [list(map(int,input().split())) for _ in range(N)]
zero_idxs = []
maximum = 0
delta = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(N):
    for j in range(M):
        if Lst[i][j] == 0:
            zero_idxs.append((i,j))

walls = list(combinations(zero_idxs,3))
# print(walls)

def Wall(lst, number):
    global maximum

    for ls in walls[number]:
        lst[ls[0]][ls[1]] = 1

    zero_cnt = 0
    Queue = deque()
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 2:
                Queue.append((i,j))
            elif lst[i][j] == 0:
                zero_cnt += 1


    while Queue:
        q = Queue.popleft()
        for dt in delta:
            x,y = q[0]+dt[0], q[1]+dt[1]
            if 0<=x<N and 0<=y<M and lst[x][y] == 0:
                Queue.append((x,y))
                lst[x][y] = 2
                zero_cnt -= 1
            if zero_cnt < maximum:
                return
    
    if maximum < zero_cnt:
        maximum = zero_cnt

    return

for num in range(len(walls)):
    Wall(copy.deepcopy(Lst), num)

print(maximum)









