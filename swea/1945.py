# 1945. 간단한 소인수분해

for tc in range(1, int(input()) + 1):
    N = int(input())
    N2, N3, N5, N7, N11 = 0, 0, 0, 0, 0
    a, b, c, d, e = 0, 0, 0, 0, 0

    while N%2 == 0:
        N = N/2
        a += 1

    while N%3 == 0:
        N = N/3
        b += 1

    while N%5 == 0:
        N = N/5
        c += 1

    while N%7 == 0:
        N = N/7
        d += 1

    while N%11 == 0:
        N = N/11
        e += 1

    print(f'#{tc} {a} {b} {c} {d} {e}')