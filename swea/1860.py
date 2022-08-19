# 1860. 진기의 붕어빵

for tc in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    N_lst = sorted(list(map(int,input().split())))

    bread = []
    for s in N_lst:
        circle = s//M
        bread.append(circle*K)

    out = "Possible"

    for i in range(len(bread)):
        if bread[i] < i+1:
            out = "Imp"+out[1:]
            break

    print(f'#{tc} {out}')