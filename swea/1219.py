# 그래프 경로. 방향성 그래프.

for tc in range(1, 11):
    tc, Nodes = map(int, input().split())

    walk = list(map(int,input().split()))
    lst = []
    for i in range(len(walk)//2):
        lst.append((walk[2*i],walk[2*i+1]))

    N, M = 0, 99  # N -> M

    visited = []
    path = []

    while True:
        available = []
        for tu in lst:
            if (tu[0] == N) and (tu not in visited):
                available.append(tu)

        if len(available) == 0 and len(path) == 1:  # 가능하지도, 갈곳도 없으면.
            print(f'#{tc} 0')
            break

        elif len(available) == 0:  # 갈길이 없으면, 갈림길까지 돌아와.
            del path[-1]
            if len(path) >= 1:
                N = path[-1][1]

        else:
            go = available[0]
            visited.append(go)
            path.append(go)
            N = go[1]

            if path[-1][1] == M:
                print(f'#{tc} 1')
                break
