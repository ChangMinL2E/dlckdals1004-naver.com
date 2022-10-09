# BOJ_15666 N과M (12)

def Backtracking(lst,k,M,pre_idx):
    if k == M:
        total_lst.append(tuple(lst[:]))
        return

    for i in range(pre_idx,N):
            lst.append(Lst[i])
            Backtracking(lst,k+1,M,i)
            lst.pop()


N, M = map(int,input().split())
Lst = sorted(list(map(int,input().split())))
total_lst = []

for idx in range(N):
    Backtracking([Lst[idx]],1,M,idx)

for ls in sorted(list(set(total_lst))):
    print(*ls)







