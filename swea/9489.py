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

    # N x M -> M x N
    lst2 = []

    for k in range(M): # lst2에 M행 생성
        lst2.append([0]* N)
    

    for l in range(N): # N열 생성해야한다.
        for k in range(M):
            lst2[k][l] = lst[l][k]


    for ls in lst2:
        for j in ls:
            if j == 1:
                total += 1
            else:
                total = 0

            if maximum < total:
                maximum = total
        total = 0

    print(f'#{tc} {maximum}')
