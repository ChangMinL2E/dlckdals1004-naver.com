# T = 1
T = int(input())

for tc in range(1,T+1):
    N1 = input()
    N2 = input()
    total = 0
    for n1 in N1:
        if N2.count(n1) > total:
            total = N2.count(n1)

    print(f'#{tc} {total}')


