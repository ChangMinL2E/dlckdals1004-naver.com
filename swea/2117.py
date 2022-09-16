# swea 2117 홈 방범 서비스

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0
    for x in range(N):
        for y in range(N):

            for K in range(N+1): # K = 0~N-1
                cnt = 0
                for i in range(K + 1): # i = 0~K
                    for j in range(i + 1): # j = 0~i
                        x_a, y_a = j, i - j
                        if x_a==0 and y_a == 0 and lst[x][y]: # 처음 가운데,
                            cnt += 1

                        elif x_a!=0 and y_a!=0:
                            if 0 <= x + x_a <= N - 1 and 0 <= y + y_a <= N - 1 and lst[x + x_a][y + y_a]:
                                cnt += 1

                            if 0 <= x - x_a <= N - 1 and 0 <= y + y_a <= N - 1 and lst[x - x_a][y + y_a]:
                                cnt += 1

                            if 0 <= x + x_a <= N - 1 and 0 <= y - y_a <= N - 1 and lst[x + x_a][y - y_a]:
                                cnt += 1

                            if 0 <= x - x_a <= N - 1 and 0 <= y - y_a <= N - 1 and lst[x - x_a][y - y_a]:
                                cnt += 1

                        elif x_a == 0:
                            if 0<= y + y_a <= N-1 and lst[x][y+y_a]:
                                cnt += 1
                            if 0<= y - y_a <= N-1 and lst[x][y-y_a]:
                                cnt += 1

                        elif y_a == 0:
                            if 0<= x + x_a <= N-1 and lst[x+x_a][y]:
                                cnt += 1
                            if 0<= x - x_a <= N-1 and lst[x-x_a][y]:
                                cnt += 1

                K += 1
                cost = K * K + (K - 1) * (K - 1)

                if M * cnt - cost >= 0 and cnt > maximum:
                    maximum = cnt

    print(f'#{tc} {maximum}')
