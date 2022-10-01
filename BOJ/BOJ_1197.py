# BOJ_1197 최소신장트리

def prim():
    U = []
    D = [1e10]*V # key 값들
    P = [0]*V # 부모트리
    D[0] = 0 # 초기(출발) node 설정

    while len(U)<V:
        minV = 1e10
        # 확인할 노드 선정
        for i in range(V):
            if not i in U: # 들리지 않았다면,
                if D[i] < minV:
                    minV = D[i]
                    curV = i # 진행할 노드 인덱스 지정

        U.append(curV)
        for i in range(V):
            if not i in U: # 확인하지 않았던 간선들을 보겠다.
                if G[curV][i] != 1e10 and G[curV][i] < D[i]: # 간접해있고, 가중치가 key보다 작으면,
                    P[i] = curV
                    D[i] = G[curV][i]

    # print(U,D,P)
    return sum(D)



V, E = map(int,input().split())
G = [[1e10]*V for _ in range(V)] # 그래프 생성
for _ in range(E):
    a,b,c = map(int,input().split())
    G[a-1][b-1] = c
    G[b - 1][a - 1] = c

print(prim())








