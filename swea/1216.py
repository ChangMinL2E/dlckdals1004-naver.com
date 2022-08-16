# 1216. 회문2

import sys

sys.stdin = open('1216.txt')

for tc in range(1, 11):
    N2 = input()
    Matrix = []
    maximum = 0
    for _ in range(100):
        N = input()
        Matrix.append(list(N))

    for row in Matrix:
        for i in range(100):
            for N in range(100 - i, 1, -1):
                test = row[i:i + N]
                if test == test[::-1]:
                    if maximum < len(test):
                        maximum = len(test)
                        break

    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if i > j:
                Matrix[i][j], Matrix[j][i] = Matrix[j][i], Matrix[i][j]

    for row in Matrix:
        for i in range(100):
            for N in range(100 - i, 1, -1):
                test = row[i:i + N]
                if test == test[::-1]:
                    if maximum < len(test):
                        maximum = len(test)
                        break

    print(f'#{tc} {maximum}')