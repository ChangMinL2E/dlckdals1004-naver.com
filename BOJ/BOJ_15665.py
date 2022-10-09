# BOJ_15665 N과 M (11)

def Backtracking(lst,k,M):
    if k == M:
        total_lst.append(tuple(lst[:]))
        return

    for i in range(N):
        lst.append(Lst[i])
        Backtracking(lst,k+1,M)
        lst.pop()

N, M = map(int,input().split())
Lst = list(map(int,input().split()))
Lst.sort()
total_lst = []

for idx in range(N):
    Backtracking([Lst[idx]],1,M)

for ls in sorted(list(set(total_lst))):
    print(*ls)












