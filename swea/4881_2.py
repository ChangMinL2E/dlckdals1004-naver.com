def per(lst, k, N, curSum):
    global minimum

    if curSum > minimum:
        return

    if k == N:
        if curSum < minimum:
            minimum = curSum
        return

    else:
        for i in range(N): # 0~N-1
            if not visited[i]:
                visited[i] = True
                per(lst, k+1, N, curSum + lst[i][k]) #
                visited[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    Matrix = []
    for _ in range(N):  # NxN 배열 생성
        Matrix.append(list(map(int, input().split())))

    minimum = 10**8
    result = [-1] * N
    visited = [False] * N
    per(Matrix, 0, N, 0)

    print(f'#{tc} {minimum}')
