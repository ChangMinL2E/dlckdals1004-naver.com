# 1251 하나로
# E: 환경부담 세율

def distance(a,b):
    return abs((a[0]-b[0])**2+(a[1]-b[1])**2)#**(1/2)

def Backtracking(Total, lst,k,N,curSum):
    global minimum

    if minimum <= curSum:
        return

    if k==N-1 and len(set(Total)) == N:
        if minimum > curSum:
            minimum = curSum
        return

    for i in range(N-1):
        for j in range(i+1,N):
            if not (i,j) in lst:
                lst.append((i,j))
                Total.append(Lst[i])
                Total.append(Lst[j])
                Backtracking(Total, lst, k+1, N, curSum +distance(Lst[i],Lst[j]))
                Total.pop()
                Total.pop()
                lst.pop()



for tc in range(1,int(input())+1):
    N = int(input())
    lst_X = list(map(int,input().split()))
    lst_Y = list(map(int,input().split()))
    Lst = []
    minimum = 1e10
    for i in range(N):
        Lst.append((lst_X[i],lst_Y[i]))


    E = float(input())

    # print(Lst)
    for i in range(N-1):
        for j in range(i+1,N):
            Backtracking([Lst[i],Lst[j]],[(i,j)],1,N,distance(Lst[i],Lst[j]))

    print(f'#{tc} {round(minimum*E)}')