# BOJ_2012 등수 매기기  
import sys
input = sys.stdin.readline
total = 0
N = int(input())

Lst = []
for _ in range(N):
    Lst.append(int(input()))

Lst.sort()
visited = [False]*N
minimum = 1e10

def rec(k,N,curSum):
    global minimum

    if curSum > minimum:
        return

    if k == N:
        if minimum > curSum:
            minimum = curSum
        return

    for id in range(N):
        if not visited[id]:
            visited[id] = True
            rec(k+1,N,curSum+abs(Lst[id]-(i+1)))
            visited[id] = False

for i in range(N):
    visited[i] = True
    rec(1,N,abs(Lst[i]-1))
    visited[i] = False

print(minimum)
