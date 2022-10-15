# BOJ_1147 RGB거리 / DP

N = int(input())

Lst = [list(map(int,input().split())) for _ in range(N)]

k = 1
while N-k:
    for i in range(3):
        Lst[k][i] += min(Lst[k-1][(i+1)%3],Lst[k-1][(i+2)%3])
    k+=1

print(min(Lst[-1]))






