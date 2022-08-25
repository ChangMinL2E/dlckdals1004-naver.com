# 5097 회전

def rotation(lst):  # 나중에 함수에 매개변수로 n을 추가해보자.
    for i in range(len(lst)):
        if i == 0:
            temp = lst[0]
        else:
            lst[i - 1] = lst[i]
    lst[len(lst) - 1] = temp


for tc in range(1, int(input()) + 1):
    M, N = map(int, input().split())
    Lst = list(map(int, input().split()))

    for _ in range(N):
        rotation(Lst)

    print(f'#{tc} {Lst[0]}')
