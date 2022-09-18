# 05 백트래킹 5209_최소 생산 비용

def Backtracking(lst, k, n, curSum):
    global minimum

    if k == n:
        if curSum < minimum:
            minimum = curSum
        return

    if curSum >= minimum:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            Backtracking(lst, k+1, n, curSum+lst[k][i])
            visited[i] = False

for tc in range(1, int(input())+1):
    N = int(input())
    lst = []
    minimum = 1000000
    visited = [False]*N
    for _ in range(N):
        lst.append(list(map(int,input().split())))

    Backtracking(lst, 0, N, 0)

    print(f'#{tc} {minimum}')


