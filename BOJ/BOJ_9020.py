# BOJ_9020 골드바흐의 추측
import sys

lst = []
visited = [False]*20000
visited[0] = True
visited[1] = True
for i in range(2,20000):
    if not visited[i]:
        lst.append(i)
        for j in range(1,20000//i):
            visited[i*j] = True

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    for num in range(N//2,1,-1):
        if num in lst and N-num in lst:
            print(num, N-num)
            break






