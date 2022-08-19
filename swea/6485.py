# 6485. 삼성시의 버스 노선

for tc in range(1, int(input()) + 1):
    N = int(input())
    A_B = []  # ex) [[1,3],[2,5]]
    for _ in range(N):
        A_B.append(list(map(int, input().split())))

    P = int(input())  # P = 5
    C_index = []  # C1=1,...,C5=5
    for _ in range(P):
        C_index.append(int(input()))
    #
    # maximum = 0
    # for c_id in C_index:
    #     if maximum < c_id:
    #         maximum = c_id
    #
    C = [0] * P  # 정류장 지나는 버스 노선갯수 측정기
    # # C = [0,1,2,2,1,1]

    for a_b in A_B:
        for idx in range(len(C_index)):
            if a_b[0] <= C_index[idx] <= a_b[1]:
                C[idx] += 1

    sol = ''
    for c in C:
        sol += str(c) + ' '

    print(f'#{tc} {sol}')
