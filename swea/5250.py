# 최소비용
from collections import deque

# def Backtracking(lst,cnt,which):
#     global minimum
#
#     if minimum < cnt:
#         return
#
#     if which == (N-1,N-1):
#         if minimum > cnt:
#             minimum = cnt
#         return
#
#     for dt in delta:
#         x,y = which[0]+dt[0],which[1]+dt[1]
#         if 0<=x<N and 0<=y<N and not visited[x][y]:
#             visited[x][y] = True
#             Backtracking(lst, cnt+1+abs(lst[which[0]][which[1]]-lst[x][y]), (x,y))
#             visited[x][y] = False

# def BFS(lst):
#     Queue = deque()
#     Queue.append((0,0,0)) # x,y,cnt
#     while Queue:
#         q = Queue.popleft()
#
#         for dt in delta:
#             x, y = q[0]+dt[0],q[1]+dt[1]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] > q[2]+1+abs(lst[q[0]][q[1]] - lst[x][y]):
#                 Queue.append((x,y,q[2] + 1 + abs(lst[q[0]][q[1]] - lst[x][y])))
#                 visited[x][y] = q[2] + 1 + abs(lst[q[0]][q[1]] - lst[x][y])
#
#     return visited[N-1][N-1]


for tc in range(1,int(input())+1):
    N = int(input())
    Lst = [list(map(int,input().split())) for _ in range(N)]
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[1e10]*N for _ in range(N)]

    Queue = deque()
    Queue.append((0, 0))  # x,y,cnt
    visited[0][0] = 0
    while Queue:
        q = Queue.popleft()

        for dt in delta:
            x, y = q[0] + dt[0], q[1] + dt[1]

            if 0 <= x < N and 0 <= y < N:
                if Lst[x][y] - Lst[q[0]][q[1]] < 0:
                    alpha = 0
                else:
                    alpha = Lst[x][y] - Lst[q[0]][q[1]]

                if visited[x][y] > visited[q[0]][q[1]] + 1 + alpha:
                    Queue.append((x, y))
                    visited[x][y] = visited[q[0]][q[1]] + 1 + alpha

    print(f'#{tc} {visited[N-1][N-1]}')





'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''

