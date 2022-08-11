T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = []
    lst.append([1] * (N+2))
    for _ in range(N):
        N2 = list(map(int, '1' + input() + '1'))
        lst.append(N2)
    lst.append([1] * (N+2))
    # print(lst)

    path = []
    visited = []

    for i in range(N+2):
        for j in range(N+2):
            if lst[i][j] == 2:
                pos = (i, j)
                path.append(pos)
                visited.append(pos)

    # print(path)

    while True:
        x, y = path[-1]
        targets = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        available = [t for t in targets if t not in visited and lst[t[0]][t[1]] != 1]

        if len(available) == 0 and len(path) == 1:
            out = f'#{tc} 0'
            break

        elif len(available) == 0:
            # if path[-1] != pos:
            del path[-1]


        else:
            v = available[0]
            path.append(v)
            visited.append(v)

            if lst[v[0]][v[1]] == 3:
                out = f'#{tc} 1'
                break

    print(out)
