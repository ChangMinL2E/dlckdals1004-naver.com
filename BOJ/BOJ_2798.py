# BOJ_2798 블랙잭

import sys
input = sys.stdin.readline

def rec(k,N1,curSum):
    global maximum

    if curSum > M:
        return

    if k == N1:
        if maximum <= curSum:
            maximum = curSum
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            rec(k+1,N1,curSum+Lst[i])
            visited[i] = False


maximum = 0
N,M = map(int,input().split())
Lst = list(map(int,input().split()))
visited = [False]*N

rec(0,3,0)

print(maximum)