# 9489. 고대유적

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = []

    for _ in range(N):
        lst.append(list(map(int, input().split())))

    maximum = 0
    total = 0
    for ls in lst:
        for j in ls:
            if j == 1:
                total += 1
            else:
                total = 0

            if maximum < total:
                maximum = total
        total = 0

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i > j:
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]

    for ls in lst:
        for j in ls:
            if j == 1:
                total += 1
            else:
                total = 0

            if maximum < total:
                maximum = total
        total = 0

    print(f'#{tc} {maximum}')
