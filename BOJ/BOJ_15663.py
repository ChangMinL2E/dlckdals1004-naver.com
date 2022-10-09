# BOJ_15663 N과 M (9)

def Backtracking(lst,k,M):
    if k == M:
        # if not lst in total_lst:
        total_lst.append(tuple(lst[:]))
            # print(*lst)
        return

    # overlap = 0
    for i in range(N):
        if not visited[i]: # and overlap != Lst[i]:
            lst.append(Lst[i])
            visited[i] = True
            # overlap = Lst[i]
            Backtracking(lst,k+1,M)
            visited[i] = False
            lst.pop()

N, M = map(int,input().split())
Lst = list(map(int,input().split()))
Lst.sort()
total_lst = []
visited = [False]*N

for idx in range(N):
    visited[idx] = True
    Backtracking([Lst[idx]],1,M)
    visited[idx] = False

for ls in sorted(list(set(total_lst))):
    print(*ls)




