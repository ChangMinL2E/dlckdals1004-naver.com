# BOJ_15649 N과 M(1)

import sys

N,M = map(int,sys.stdin.readline().split())
visited = [False]*(N+1)
lst = []
def Backtracking(lst,k,num):
    if k == num:
        print(*lst)
        return

    for i in range(1,N+1):
        if not visited[i]:
            lst.append(i)
            visited[i] = True
            Backtracking(lst, k+1, num)
            visited[i] = False
            lst.pop()

Backtracking(lst, 0, M)



