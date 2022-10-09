# BOJ_15664 N과 M (10)

def Backtracking(lst,k,M,pre):
    if k == M:
        total_lst.append(tuple(lst[:]))
        return

    for i in range(pre+1,N):
        if not visited[i]:
            lst.append(Lst[i])
            visited[i] = True
            Backtracking(lst,k+1,M,i)
            visited[i] = False
            lst.pop()

N, M = map(int,input().split())
Lst = list(map(int,input().split()))
Lst.sort()
total_lst = []
visited = [False]*N

for idx in range(N):
    visited[idx] = True
    Backtracking([Lst[idx]],1,M,idx)
    visited[idx] = False

for ls in sorted(list(set(total_lst))):
    print(*ls)





