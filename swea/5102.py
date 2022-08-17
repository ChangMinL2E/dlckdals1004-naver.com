# 노드의 거리
# DFS가 아니라 BFS로 구현해야하나.


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    lst = []
    for _ in range(E):  # 갈수 있는 노선 모음.
        s, e = map(int, input().split())
        lst.append((s, e)) # 방향성 노선이 아니라 양방향.
        lst.append((e, s))

    N, M = map(int, input().split())  # N -> M 가는데 얼마나 걸리는지.

    visited = []
    path = []
    sol = []
    path_last = []
    N2 = N
    minimum = 0

    cml = True
    while cml:
        available = []
        for tu in lst:
            if (tu[0] == N2) and (tu not in visited) and (tu[::-1] not in visited) and (tu not in path_last):
                available.append(tu)

        if len(available) == 0 and len(path) == 1:  # 가능하지도, 갈곳도 없으면.
            if len(sol) == 0:
                print(f'#{tc} 0')
            else:
                for solution in sol:
                    if minimum > len(solution):
                        minimum = len(solution)
                        cml = False

        elif len(available) == 0:  # 갈길이 없으면, 갈림길까지 돌아와.
            del path[-1]
            if len(path) >= 1:
                N2 = path[-1][1]

        else:
            go = available[0]
            visited.append(go)
            path.append(go)
            N2 = go[1]

            if path[-1][1] == M:
                path_last.append(path[-1])
                sol.append(path)
                N2 = N
                path = [] # 초기화
                visited = []
                # print(f'#{tc} {len(path)}')
                # break
