# BOJ_15650 N과 M(2)

import sys

N,M = map(int,sys.stdin.readline().split())
visited = [0]*(N+1)
lst = []
total_lst = []
def Backtracking(lst,k,num):
    if k == num:
        if not set(lst) in total_lst:
            total_lst.append(set(lst))
            print(*lst)
        return

    for i in range(1,N+1):
        if not visited[i]:
            lst.append(i)
            visited[i] += 1
            Backtracking(lst, k+1, num)
            visited[i] = False
            lst.pop()

Backtracking(lst, 0, M)



