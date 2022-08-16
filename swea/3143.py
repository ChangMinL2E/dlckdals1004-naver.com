# 3143. 가장 빠른 문자열 타이핑

T = int(input())
for tc in range(1, T + 1):
    total, sub = input().split()
    out = 0
    cnt = 0
    # total_lst = list(total)
    # sub_lst = list(sub)
    cml = True
    i = 0
    N = len(sub)

    while cml:
        if i+N > len(total):
            cml = False

        elif total[i:i+N] == sub:
            cnt += 1
            i = i+N

        else:
            i += 1



    out = len(total) - (len(sub) - 1) * cnt

    print(f'#{tc} {out}')
