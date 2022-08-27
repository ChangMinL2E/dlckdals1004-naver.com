# BOJ_2635 수 이어가기

def Go(num):
    MX_lst = []
    for i in range(1,num+1):
        lst = []
        cnt = 2
        lst.append(num)
        lst.append(i)
        cml = True
        while cml:
            lst.append(0)
            lst[cnt] = lst[cnt-2] - lst[cnt-1]
            if lst[cnt] < 0:
                # lst[cnt] = -1 * lst[cnt]
                lst.pop()
                cml = False
            else:
                cnt += 1
        if len(MX_lst) < len(lst):
            MX_lst = lst
    print(len(MX_lst))
    print(*MX_lst)


Go(int(input()))

