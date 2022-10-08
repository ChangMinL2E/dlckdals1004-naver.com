# BOJ_2992 크면서 작은 수 / Backtracking

def Backtracking(k,N,present):
    if k==N:
        if int(present) >= standard:
            Lst.append(int(present))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            Backtracking(k+1,N,present+lst[i])
            visited[i] = False



lst = list(input())
Lst = []
standard = int(''.join(lst))

visited = [False]*(len(lst))
for idx in range(len(lst)):
    visited[idx] = True
    Backtracking(1,len(lst),lst[idx])
    visited[idx] = False
Lst = sorted(list(set(Lst)))

if len(Lst) == 1:
    print(0)
else:
    print(Lst[1])







