# 1244 최대상금


for tc in range(1,int(input())+1):
    A, N = map(int,input().split())
    lst = list(map(int,str(A)))
    sol_lst = sorted(lst, reverse=True)
    cml = True
    cnt = 0
    k = 0
    while cml:
        if k == N:
            cml = False

        if sol_lst != lst and cnt < len(lst): # 목표 리스트와 같은지.
            if lst[cnt] != sol_lst[cnt]:
                for i in range(len(lst)-1,-1,-1):
                    if lst[i] == sol_lst[cnt]:
                        lst[cnt], lst[i] = lst[i], lst[cnt]
                        cnt += 1
                        k += 1
                        break
            else:
                cnt += 1

        else:
            if (N - k) % 2:
                lst[-2], lst[-1] = lst[-1], lst[-2]
                cml = False
            else:
                cml = False

    for idx in range(len(lst)):
        lst[idx] = str(lst[idx])
    # sol = str("".join(lst))

    print(f'#{tc} {str("".join(lst))}')
