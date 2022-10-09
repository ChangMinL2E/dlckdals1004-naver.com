# BOJ_15657 N과 M (8)

def per(lst,k,M,pre):
    if k == M:
        # if not sorted(lst) in total_lst:
        total_lst.append(lst[:])
        return

    for i in range(pre,N):
            lst.append(Lst[i])
            per(lst,k+1,M,i)
            lst.pop()


N, M = map(int,input().split())
Lst = list(map(int,input().split()))
visited_lst = []
visited = [False]*N
total_lst = []
Lst.sort()
for idx in range(N):
    per([Lst[idx]],1,M,idx)


for ls in total_lst:
    print(*ls)






