# BOJ_4948 베르트랑 공준

import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    total = 0
    for i in range(N + 1, 2 * N + 1):
        if i == 1:
            print(2)
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                total += 1
    print(total)
