# 1,2,3 더하기 / backtracking

def Backtracking(lst,N,CurSum):
    if CurSum > N:
        return

    if N == CurSum:
        Lst.append(lst)
        return

    for i in range(1,4):
        lst.append(i)
        Backtracking(lst,N,CurSum+i)
        lst.pop()


n, k = map(int,input().split())
Lst = []

for i in range(1,4):
    Backtracking([i],n,i)

print(Lst)









