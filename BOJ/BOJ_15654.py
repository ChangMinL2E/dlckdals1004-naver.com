# BOJ_15654 N과 M (5)

def per(lst,k,M):
    if k == M:
        print(*lst)
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
visited = [False]*N
Lst.sort()
for idx in range(N):
    visited[idx] = True
    per([Lst[idx]],1,M)
    visited[idx] = False





