# 노드의 거리

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    lst = []
    for _ in range(E):  # 갈수 있는 노선 모음.
        s, e = map(int, input().split())
        lst.append((s, e))

    N, M = map(int, input().split())  # N -> M 가는데 얼마나 걸리는지.

    visited = []
    path = []
    N2 = N

    while True:
        available = []
        for tu in lst:
            if (tu[0] == N2) and (tu not in visited):
                available.append(tu)

        if len(available) == 0 and len(path) == 1:  # 가능하지도, 갈곳도 없으면.
            out = f'#{tc} 0'
            break

        elif len(available) == 0:  # 갈길이 없으면, 갈림길까지 돌아와.
            del path[-1]
            if len(path) >= 1:
                N2 = path[-1][0]

        else:
            go = available[0]
            visited.append(go)
            path.append(go)
            N2 = go[1]

            if path[-1][1] == M:
                print(f'#{tc} {len(path)}')
                break
