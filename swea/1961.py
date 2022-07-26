# T = 10
T = int(input())

for i in range(1,T+1):
    # N = 3
    N = int(input())
    lst_in = []
    lst_out1 = [[0 for _ in range(N)] for _ in range(N)] # 각 N x N 0행렬 생성 # np.zeros((3,3))
    lst_out2 = [[0 for _ in range(N)] for _ in range(N)] 
    lst_out3 = [[0 for _ in range(N)] for _ in range(N)] 

    for j in range(N):
        N2 = input()
        N2 = map(int,N2.split())
        lst_in.append(list(N2))
    # print(lst_in)


    for k in range(N): # 90도 회전한 행렬 lst_out1
        for l in range(N):
            lst_out1[k][l] = lst_in[N-l-1][k]
    # print(lst_out1)

    for k in range(N): # 180도 회전한 행렬 lst_out2
        for l in range(N):
            lst_out2[k][l] = lst_out1[N-l-1][k]
    # print(lst_out2)

    for k in range(N): # 270도 회전한 행렬 lst_out3
        for l in range(N):
            lst_out3[k][l] = lst_out2[N-l-1][k]
    # print(lst_out3)

    print(f'#{i}')
    for idx in range(N):
        for idx2 in range(N):
            print(lst_out1[idx][idx2], end='')
        print(end=' ')
        for idx3 in range(N):
            print(lst_out2[idx][idx3], end='')
        print(end=' ')
        for idx4 in range(N):
            print(lst_out3[idx][idx4], end='')
        print()
        
