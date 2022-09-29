# Dijkstra

'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''


def dijkstra():
    U = []
    D = [10000] * (N + 1)  # infinite 대신 10000을 적어줬다.
    P = [10000] * (N + 1)
    D[0] = 0
    while len(U) < N + 1:
        # D에서 최소를 구한다.(단, U에 포함되지 않은 것을 대상으로
        minV = 10000
        for i in range(N + 1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # i와 연결된 정점들의 D를 수정
        for i in range(N + 1):
            if i in U: continue
            # if G[curV][i] and D[i] > D[curV] + G[curV][i]:
            #     D[i] = G[curV][i]
            #     P[i] = curV
            if G[curV][i]:
                D[i] = min(D[i], D[curV]+G[curV][i])
                P[i] = curV

    print(U, D, P)


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]  # 인접행렬

for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w
    # G[n2][n1] = w
print(G)
dijkstra()
