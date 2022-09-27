# 1865. 동철이의 일 분배 / Backtracking

def per(k,N,curSum):
    global maximum

    if curSum == 0 or curSum < maximum:
        return

    if k == N:
        if round(curSum,6) > maximum:
            maximum = curSum
        return

    for idx in range(N):
        if not visited[idx]:
            visited[idx] = True
            per(k+1, N, curSum*lst[k][idx]/100)
            visited[idx] = False

for tc in range(1,int(input())+1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int,input().split())))
    maximum = 0
    visited = [False]*N

    for i in range(N):
        visited[i] = True
        per(1,N,lst[0][i])
        visited[i] = False

    print(f'#{tc} {maximum:6f}')






