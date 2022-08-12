# 12712. 파리퇴치 3

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    lst = []
    for _ in range(M - 1):
        lst.append([0] * (N + 2*(M-1)))

    for _ in range(N):
        N2 = input()
        N3 = '0 ' * (M - 1) + N2 + ' 0' * (M - 1)
        lst_N3 = list(map(int, N3.split()))
        lst.append(lst_N3)

    for _ in range(M - 1):
        lst.append([0] * (N + 2*(M-1)))

    total = 0
    maximum = 0
    for x in range(M-1, N + M - 1):
        for y in range(M-1, N + M - 1):
            for j in lst[y][x - (M - 1):x + M]:
                total += j
            for k in lst[y-(M-1):y+M]:
                total += k[x]
            total -= lst[y][x]
            if maximum < total:
                maximum = total
            total = 0

    for x in range(M - 1, N + M - 1):
        for y in range(M - 1, N + M - 1):
            for i in range(M):
                total += lst[y-i][x-i] + lst[y-i][x+i] + lst[y+i][x-i] + lst[y+i][x+i]
            total -= 3*lst[y][x]
            if maximum < total:
                maximum = total
            total = 0


    print(f'#{tc} {maximum}')

