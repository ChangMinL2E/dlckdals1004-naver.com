# BOJ_15486 퇴사 2

import sys
input = sys.stdin.readline



N = int(input())
Lst = [0]*(N+1)
T = []
P = []
for _ in range(N):
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)

for i in range(N):
    if i + T[i] < N+1:
        # Lst[i+T[i]] = max(Lst[i+T[i]],Lst[i]+P[i])
        for j in range(i,N):
            if j + T[i] < N+1:
                Lst[j+T[i]] = max([Lst[j+T[i]],Lst[i]+P[i]])

print(max(Lst))
# print(Lst)

