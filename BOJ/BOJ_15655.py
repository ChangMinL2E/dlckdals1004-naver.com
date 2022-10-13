# BOJ_15655 N과 M (6)

def per(lst,k,M):
    if k == M:
        if not visited in visited_lst:
            visited_lst.append(visited[:])
            total_lst.append(lst[:])
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            lst.append(Lst[i])
            per(lst,k+1,M)
            lst.pop()
            visited[i] = False


N, M = map(int,input().split())
Lst = list(map(int,input().split()))
visited_lst = []
visited = [False]*N
total_lst = []
Lst.sort()
for idx in range(N):
    visited[idx] = True
    per([Lst[idx]],1,M)
    visited[idx] = False

for ls in total_lst:
    print(*ls)





