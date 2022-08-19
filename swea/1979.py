# 1979. 단어

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    Matrix = []
    Matrix.append([0] * (N + 2))
    for _ in range(N):
        lst = [0]
        input1 = list(map(int, input().split()))
        Matrix.append(lst + input1 + lst)
    Matrix.append([0] * (N + 2))

    cnt = 0
    sol = [0]  # 정답지
    for _ in range(K):
        sol.append(1)
    sol.append(0)

    for mat in Matrix:  # 가로 검사
        for i in range(N-K+1):
            if mat[i:i + K + 2] == sol:
                cnt += 1

    for i in range(N + 2):
        for j in range(N + 2):
            if i > j:
                Matrix[i][j], Matrix[j][i] = Matrix[j][i], Matrix[i][j]

    for mat in Matrix:  # 세로 검사
        for i in range(N-K+1):
            if mat[i:i + K + 2] == sol:
                cnt += 1

    print(f'#{tc} {cnt}')