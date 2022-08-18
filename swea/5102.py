# 노드의 거리
# DFS가 아니라 BFS로 구현해야하나.

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    lst = []
    for _ in range(E):  # 갈수 있는 노선 모음.
        s, e = map(int, input().split())
        lst.append((s, e))
        lst.append((e, s))

    N, M = map(int, input().split())  # N -> M 가는데 얼마나 걸리는지.

    visited = []
    queue = []
    cnt = 1

    for start, end in lst:
        if start == N:
            queue.append((start, end, 1))
            visited.append((start, end))

    cml = True

    while cml:
        available = []
        for tu2 in queue:
            N2 = tu2[1]  # 끝나는 지점을 다음 시작 지점으로 가지는 노선을 모두 모으겠다.
            for tu in lst:
                if (tu[0] == N2) and (tu not in visited):
                    available.append(tu)
                    visited.append(tu)

        if len(available) == 0:  # 가능하지도, 갈곳도 없으면.
            print(f'#{tc} 0')
            cml = False

        else:
            cnt += 1
            for k, l in available:
                queue.append((k, l, cnt))
                visited.append((k, l))

            for ele in queue:
                if ele[1] == M:
                    print(f'#{tc} {ele[2]}')
                    cml = False
