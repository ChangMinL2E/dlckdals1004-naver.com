# def re(value):
#     pass
#
#
# def re1(stIdx, edIdx):
#     pass
#
#
# lst = [0, 10, 2, 3, 4, 5, 6, 7]
# st = 0
# ed = 7
# re(lst[0:3])
# re1(st, (st + ed) // 2)

def fight(W, B):
    if lst[W] - lst[B] == 1 or lst[W] - lst[B] == -2:
        return W
    elif lst[B] - lst[W] == 1 or lst[B] - lst[W] == -2:
        return B
    else:
        return W


def divide(st, ed):
    if st == ed:
        return st

    a = divide(st, (st + ed) // 2)
    b = divide((st + ed) // 2 + 1, ed)
    return fight(a, b)


for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{tc} {divide(0, N - 1) + 1}')
