# T = 1
T = int(input())

for tc in range(1, T + 1):
    N1 = input()
    N2 = input()
    dic = {}

    for key in N1:
        dic[key] = 0

    for n2 in N2:
        if n2 in N1:
            dic[n2] += 1

    total = 0

    for key in N1:
        if dic[key] > total:
            total = dic[key]

    print(f'#{tc} {total}')
