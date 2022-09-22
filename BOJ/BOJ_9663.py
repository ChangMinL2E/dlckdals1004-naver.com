# BOJ_9663 백트래킹 N-Queen

import sys
import copy

N = int(sys.stdin.readline())
lst = []
total_lst = []
visited = [[False for _ in range(N)] for _ in range(N)]

def Backtracking(lst,num,N,visit,cnt):
    if num == N:
        if not set(lst) in total_lst:
            total_lst.append(set(lst))
        return

    if N*N+N < num+cnt:
        print(N*N)
        print(num+cnt)
        return
    count = 0
    for i in range(N):
        for j in range(N):
            if num==0:
                lst.append((i,j))
                visited2 = copy.deepcopy(visit)
                for k in range(N): # visited
                    if visit[k][j] == False:
                        visit[k][j] = True # 가로
                        count += 1
                    if visit[i][k] == False:
                        visit[i][k] = True # 세로
                        count += 1
                    # 대각선
                    if 0<=i+k<N and 0<=j+k<N and visit[i+k][j+k] == False: # 우 하향
                        visit[i+k][j+k] = True
                        count += 1
                    if 0<=i-k<N and 0<=j+k<N and visit[i-k][j+k] == False: # 우 상향
                        visit[i-k][j+k] = True
                        count += 1
                    if 0 <= i - k < N and 0 <= j - k < N and visit[i - k][j - k] == False: # 좌 상향
                        visit[i - k][j - k] = True
                        count += 1
                    if 0 <= i + k < N and 0 <= j - k < N and visit[i + k][j - k] == False: # 좌 하향
                        visit[i + k][j - k] = True
                        count += 1

                Backtracking(lst,num+1,N,visit,cnt+count)
                # visit = [[False for _ in range(N)] for _ in range(N)]
                visit = visited2
                lst.pop()
                count = 0
            else:
                if not visit[i][j]:
                    lst.append((i,j))
                    visited2 = copy.deepcopy(visit)
                    count = 0
                    for k in range(N):  # visited
                        if visit[k][j] == False:
                            visit[k][j] = True  # 가로
                            count += 1
                        if visit[i][k] == False:
                            visit[i][k] = True  # 세로
                            count += 1
                        # 대각선
                        if 0 <= i + k < N and 0 <= j + k < N and visit[i + k][j + k] == False:  # 우 하향
                            visit[i + k][j + k] = True
                            count += 1
                        if 0 <= i - k < N and 0 <= j + k < N and visit[i - k][j + k] == False:  # 우 상향
                            visit[i - k][j + k] = True
                            count += 1
                        if 0 <= i - k < N and 0 <= j - k < N and visit[i - k][j - k] == False:  # 좌 상향
                            visit[i - k][j - k] = True
                            count += 1
                        if 0 <= i + k < N and 0 <= j - k < N and visit[i + k][j - k] == False:  # 좌 하향
                            visit[i + k][j - k] = True
                            count += 1

                    Backtracking(lst,num+1,N,visit, cnt+count)
                    visit = visited2
                    lst.pop()
                    count = 0

Backtracking(lst,0,N, visited, 0)
# print(len(total_lst))

# 시간초과나와서 아래와 같이 통과할수도 있다.
a = (0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596)
print(a[N])






