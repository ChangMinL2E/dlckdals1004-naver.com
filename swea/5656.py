# 0927 A형 테스트 / 벽돌깨기
# save

from collections import deque
import copy


def per(lst, k, N, bomb):
    global minimum

    if minimum == 0:
        return

    if k + 1 == N:
        cnt = W * H
        for idx in range(H):
            cnt -= lst[idx].count(0)
        if minimum > cnt:
            minimum = cnt
        return

    Queue = deque()
    Queue.append(bomb)  # tuple bomb
    while Queue:
        q = Queue.popleft()
        scope = lst[q[0]][q[1]]
        if scope == 1:
            lst[q[0]][q[1]] = 0

        else:
            lst[q[0]][q[1]] = 0
            for i in range(scope):  # 가로 q[0] , q[1]+- i
                if 0 <= q[1] + i < W:
                    if lst[q[0]][q[1] + i] > 1:
                        Queue.append(q)
                    else:
                        lst[q[0]][q[1] - i] = 0
                if 0 <= q[1] - i < W:
                    if lst[q[0]][q[1] - i] > 1:
                        Queue.append(q)
                    else:
                        lst[q[0]][q[1] - i] = 0
            # 세로
            for j in range(scope):
                if 0 <= q[0] + j < H:
                    if lst[q[0] + j][q[1]] > 1:
                        Queue.append(q)
                    else:
                        lst[q[0] + j][q[1]] = 0
                if 0 <= q[0] - j < H:
                    if lst[q[0] - j][q[1]] > 1:
                        Queue.append(q)
                    else:
                        lst[q[0] - j][q[1]] = 0

        # 벽돌 다 깨고, 벽돌 내리기

        for col_idx in range(W):
            cml = True
            zero_idx = H - 1
            while cml:
                while lst[zero_idx][col_idx]:  # 0일때까지.
                    zero_idx -= 1

                nonzero_idx = zero_idx
                for i in range(1, zero_idx + 1):
                    if lst[zero_idx - i][col_idx]:
                        nonzero_idx = zero_idx - i
                        break
                lst[zero_idx][col_idx], lst[nonzero_idx][col_idx] = lst[nonzero_idx][col_idx], lst[zero_idx][col_idx]

                if not zero_idx or zero_idx == nonzero_idx:
                    cml = False

    # 내렸으면, 또 부수기
    if lst == [[0 for _ in range(W)] for _ in range(H)]:
        minimum = 0
        return

    for col in range(W):
        for row in range(1, H):
            if lst[row][col] != 0 and lst[row - 1][col] == 0:
                per(copy.deepcopy(lst), k + 1, N, (row, col))
                break


for tc in range(1, int(input()) + 1):
    bricks = []
    N, W, H = map(int, input().split())
    minimum = W * H
    for _ in range(H):
        bricks.append(list(map(int, input().split())))

    for col in range(W):
        cml2 = True
        if bricks[0][col] != 0:
            per(copy.deepcopy(bricks), 1, N, (0, col))
            cml2 = False
        if cml2:
            for row in range(1, H):
                if bricks[row][col] != 0 and bricks[row - 1][col] == 0:
                    per(copy.deepcopy(bricks), 1, N, (row, col))
                    break

    print(minimum)











