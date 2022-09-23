# swea 2382 미생물 격리

direct_dict = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(K)]

    # 0, N+1 이 경계

    while M:
        visited = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
        who = []

        # 이동
        for idx in range(len(lst)):
            if lst[idx][3] == 1:  # 이동방향이 1
                lst[idx][0] -= 1
            elif lst[idx][3] == 2:  #
                lst[idx][0] += 1
            elif lst[idx][3] == 3:
                lst[idx][1] -= 1
            elif lst[idx][3] == 4:
                lst[idx][1] += 1
            visited[lst[idx][0]][lst[idx][1]] += 1 # 카운트 하겠다.

            # 하는 김에 약품으로 가면 방향 바꿔주고, 미 생물 수 절반.
            if lst[idx][0] == 0 or lst[idx][0] == N-1 or lst[idx][1] == 0 or lst[idx][1] == N-1:
                lst[idx][3] = direct_dict[lst[idx][3]]
                lst[idx][2] = lst[idx][2]//2

        # 겹치는 미생물

        for i in range(len(visited)):
            for j in range(len(visited)):
                if visited[i][j] >= 2:
                    maximum = (-1,-1) # 미생물, index
                    who = []
                    which = []
                    for idx in range(len(lst)):
                        if lst[idx][0] == i and lst[idx][1] == j:
                            who.append(lst[idx][2]) # 미생물을 넣자.
                            which.append(idx) # 인덱스도 넣자.
                            if maximum[0] < lst[idx][2]:
                                maximum = (lst[idx][2],idx)
                    index = maximum[1]
                    # 가장 큰 군집을 따르는 원소 넣기
                    lst.append([lst[index][0], lst[index][1],sum(who),lst[index][3]])# 새로운 미생물

                    # 새로 넣고, 겹쳐진 원소들은 모두 빼기
                    for idx in range(len(which)-1,-1,-1):
                        lst.pop(which[idx])
        M -= 1
        # print(lst)

    Total = 0
    for ls in lst:
        Total += ls[2]
    print(f'#{tc} {Total}')






