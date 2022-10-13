# BOJ_15656 N과 M (7)

def per(lst,k,M):
    if k == M:
        print(*lst)
        return

    for i in range(N):
            lst.append(Lst[i])
            per(lst,k+1,M)
            lst.pop()



N, M = map(int,input().split())
Lst = list(map(int,input().split()))
Lst.sort()
for idx in range(N):
    per([Lst[idx]],1,M)










