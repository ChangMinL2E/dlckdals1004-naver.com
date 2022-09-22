# 1247. 최적 경로 / 완전 탐색

def Backtracking(lst,k,N,curSum,now):
    global minimum, start, end

    if k == N+1:
        if minimum > curSum:
            minimum = curSum
        return

    if minimum < curSum:
        return

    if k != N:
        x_now, y_now = now[0],now[1]
        for i in range(N):
            if not visited[i]:
                x_next, y_next = lst[i][0], lst[i][1]
                distance = abs(x_next-x_now)+abs(y_next-y_now)
                visited[i] = True
                Backtracking(lst, k+1, N, curSum+distance, lst[i])
                visited[i] = False

    elif k == N:
        x_now, y_now = now[0], now[1]
        x_next, y_next = end[0],end[1]
        distance = abs(x_next - x_now) + abs(y_next - y_now)
        Backtracking(lst, k+1, N, curSum+distance, end)


for tc in range(1,int (input())+1):
    minimum = 1e+8
    N = int(input())
    Input_lst = list(map(int,input().split()))
    lst = []
    for i in range(N+2):
        lst.append((Input_lst[2*i],Input_lst[2*i+1]))

    visited = [False] * N
    start = lst.pop(0)
    end = lst.pop(0)

    Backtracking(lst,0,N,0,start)
    print(f'#{tc} {minimum}')






