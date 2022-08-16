# 1859. 백만장자

def total(Lst):
    tot = 0
    for ls in Lst:
        tot += ls
    return tot


for tc in range(1, int(input()) + 1):
    L = int(input())
    lst = list(map(int, input().split()))
    revenue = 0

    while lst != []:
        maximum = 0
        max_i = 0

        for i in range(len(lst)):
            if lst[i] > maximum:
                max_i, maximum = i, lst[i]

        revenue += maximum * (max_i+1) - total(lst[:max_i+1])
        lst = lst[max_i+1:]

    print(f'#{tc} {revenue}')
