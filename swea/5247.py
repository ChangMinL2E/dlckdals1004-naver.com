# 5247 06 그래프 - 연산
# 10개중 4개 런타임에러 # 무한 루프 빠지는 경우는?


# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     visited = [-1] * 1000010
#     Queue = [N]
#     visited[N] = 0
#
#     cml = True
#     while cml:
#         Q = Queue.pop(0)
#         if Q == M:
#             result = visited[Q]
#             cml = False
#
#         Q_lst = [Q + 1, Q - 1, Q * 2, Q - 10]
#
#         for q in Q_lst:
#             if visited[q] == -1: #and q > 0:
#                 Queue.append(q)
#                 visited[q] = visited[Q] + 1
#
#     print(f'#{tc} {result}')

# 5247 06 그래프 - 연산


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visited = [False] * 1000010
    Queue = [(N,0)]
    visited[N] = True
    cnt = 0
    cml = True

    while cml:
        Q = Queue[cnt]
        if Q[0] == M:
            result = Q[1]
            cml = False

        Q_lst = [(Q[0] + 1,Q[1]), (Q[0] - 1,Q[1]), (Q[0] * 2,Q[1]), (Q[0] - 10,Q[1])]

        for q in Q_lst:
            if not visited[q[0]] and 0 < q[0] <= 1000000:
                Queue.append((q[0],q[1]+1))
                visited[q[0]] = True

        cnt += 1

    print(f'#{tc} {result}')

