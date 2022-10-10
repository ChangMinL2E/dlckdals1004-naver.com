# BOJ_1941 소문난 칠공주 / Permutation
import copy

from collections import deque

def bfs_search(lst):
    Queue = deque()
    total_Queue = deque()
    Queue.append(lst[0])
    total_Queue.append(lst[0])

    while Queue:
        q = Queue.popleft()
        for dt in delta:
            x,y = q[0]+dt[0],q[1]+dt[1]
            if not (x,y) in total_Queue and (x,y) in lst:
                Queue.append((x,y))
                total_Queue.append((x,y))

    if len(total_Queue) == 7:
        return 1
    else:
        return 0

def per(lst,k,N,num,Y_cnt):
    global count

    if Y_cnt >= 4: # Y_cnt가 4개 이상이면 그만.
        return

    if k + (25-num)< 7:# 남은 갯수 + 갈수 있는 갯수 < 7 이면 return
        return

    if k == N:
        if bfs_search(lst):
            count += 1
        return



    for idx in range(num+1,25):
        lst.append((idx//5,idx%5))
        if Lst[idx // 5][idx % 5] == 'Y':
            per(copy.deepcopy(lst),k+1,N,idx,Y_cnt+1)
        else:
            per(copy.deepcopy(lst),k+1,N,idx,Y_cnt)
        lst.pop()

delta = [(0,1),(0,-1),(1,0),(-1,0)]
count = 0
Lst = [list(input()) for _ in range(5)]
visited = [[False]*5 for _ in range(5)]
for i in range(19):
    if Lst[i//5][i%5] == 'Y':
        per([(i//5,i%5)],1,7,i,1)
    else:
        per([(i // 5, i % 5)], 1, 7, i, 0)

print(count)





