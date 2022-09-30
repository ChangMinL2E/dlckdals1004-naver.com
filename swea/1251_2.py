def distance(a,b):
    return abs((a[0]-b[0])**2+(a[1]-b[1])**2)

def prim():
    U = []
    D = [1e20]*(N) # infinite 대신 10000을 적어줬다.
    P = [1e20]*(N)
    D[0] = 0
    while len(U) < N:
        # D에서 최소를 구한다.(단, U에 포함되지 않은 것을 대상으로)
        minV = 1e20
        for i in range(N):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # i와 연결된 정점들의 D를 수정
        for i in range(N):
            if i in U: continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
                P[i] = curV
    # print(U,D,P)

    print(f'#{tc} {round(sum(D)*E)}')

for tc in range(1,int(input())+1):
    N = int(input())
    lst_X = list(map(int,input().split()))
    lst_Y = list(map(int,input().split()))
    Lst = []
    minimum = 1e10
    G = [[0] * (N) for _ in range(N)]  # 인접행렬
    for i in range(N):
        Lst.append((lst_X[i],lst_Y[i]))

    for i in range(N):
        for j in range(N):
            G[i][j] = distance(Lst[i],Lst[j])

    E = float(input())

    prim()