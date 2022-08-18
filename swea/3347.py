# 3347. 올림픽 종목 투표

for tc in range(1, int(input()) + 1):  # testcase input
    N, M = map(int, input().split())
    lst = [0] * N

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for b in B:
        for i in range(N):
            if A[i] <= b:
                lst[i] += 1
                break

    maximum = 0
    idx = 0
    for j in range(N):
        if maximum < lst[j]:
            maximum = lst[j]
            idx = j + 1

    print(f'#{tc} {idx}')
