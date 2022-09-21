# 1244 최대상금
def Backtracking(lst, k, N, cnt):
    global maximum

    if k == N:
        target_lst = lst[:]
        for idx in range(len(lst)):
            target_lst[idx] = str(target_lst[idx])
        sol = str("".join(target_lst))
        if int(sol) > maximum:
            maximum = int(sol)
        return

    if sol_lst != lst and cnt < len(lst):  # 목표 리스트와 같게 만들어지지 않았다면,
        if lst[cnt] != sol_lst[cnt]:
            for i in range(len(lst) - 1, cnt - 1, -1):
                if lst[i] == sol_lst[cnt]:
                    lst[cnt], lst[i] = lst[i], lst[cnt]
                    Backtracking(lst, k + 1, N, cnt + 1)
                    lst[cnt], lst[i] = lst[i], lst[cnt]

        else:
            Backtracking(lst, k, N, cnt + 1)

    else:  # 목표리스트와 같다면,
        if button:
            Backtracking(lst, N, N, cnt)
        else:
            if (N - k) % 2:
                lst[-2], lst[-1] = lst[-1], lst[-2]
                Backtracking(lst, N, N, cnt)
                lst[-2], lst[-1] = lst[-1], lst[-2]
            else:
                Backtracking(lst, N, N, cnt)


for tc in range(1, int(input()) + 1):
    maximum = 0
    A, N = map(int, input().split())
    Lst = list(map(int, str(A)))
    sol_lst = sorted(Lst, reverse=True)
    button = 0
    for idx in range(len(sol_lst)-1):
        if sol_lst[idx] == sol_lst[idx+1]:
            button = 1
            break
    Backtracking(Lst, 0, N, 0)

    print(f'#{tc} {maximum}')
