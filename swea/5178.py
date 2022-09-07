# swea.5178 노드의 합

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    # print(tree)

    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    for i in range(N, 0, -1):
        if tree[i] != 0:
            pass
        elif i != N // 2:
            tree[i] = tree[2 * i] + tree[2 * i + 1]
        else:  # i == N//2
            if N % 2 == 0:  # 짝수면,
                tree[N // 2] = tree[N]
            else:
                tree[N // 2] = tree[N] + tree[N - 1]

    print(f'#{tc} {tree[L]}')
