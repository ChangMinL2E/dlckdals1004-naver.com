# 1974. 스도쿠 검증

for tc in range(1, int(input()) + 1):
    Matrix = []
    for _ in range(9):
        Matrix.append(list(map(int, input().split())))  # 9 X 9 Matrix

    out = 1
    test_lst = []

    for lst in Matrix:  # row 검증
        for ls in lst:
            if ls not in test_lst:
                test_lst.append(ls)
            else:
                out = 0
        test_lst = []

    for i in range(3):  # 3x3 검증
        for j in range(3):
            # Matrix[3*i:3*i+3][3*j:3*j+3]
            for k in range(3):
                for l in range(3):
                    ele = Matrix[3 * i + k][3 * j + l]
                    if ele not in test_lst:
                        test_lst.append((Matrix[3 * i + k][3 * j + l]))
                    else:
                        out = 0
            test_lst = []

    for i in range(9):  # 스도쿠는 전치행렬도 스도쿠이다.
        for j in range(9):
            if i > j:
                Matrix[i][j], Matrix[j][i] = Matrix[j][i], Matrix[i][j]

    for lst in Matrix:  # column 검증
        for ls in lst:
            if ls not in test_lst:
                test_lst.append(ls)
            else:
                out = 0
        test_lst = []

    print(f'#{tc} {out}')
