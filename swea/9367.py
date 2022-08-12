# 9367. 점점 커지는 당근의 개수

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    total = 1
    max_total = 1
    for i in range(1, N):
        if lst[i] > lst[i - 1]:
            total += 1
            if max_total < total:
                max_total = total
        else:
            total = 1
    print(f'#{tc} {max_total}')
