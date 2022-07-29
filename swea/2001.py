# 파리 퇴치

# T = 10
T = int(input())
for tc in range(T):

# N = 5
# M = 2
    N, M = map(int,input().split())
    # print(N,M)
    Matrix = []

    for _ in range(N):
        N2 = map(int,input().split())
        N2 = list(N2)
        Matrix.append(N2)

    # print(Matrix)
    mx_total = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            test_total = 0
            for k in Matrix[i:i+M]:
                test_total += sum(k[j:j+M])
            if test_total > mx_total:
                mx_total = test_total
            # if mx_total < (Matrix[i][j] + Matrix[i][j+1] + Matrix[i+1][j] + Matrix[i+1][j+1]):
            #     mx_total = Matrix[i][j] + Matrix[i][j+1] + Matrix[i+1][j] + Matrix[i+1][j+1]

    print(f'#{tc+1} {mx_total}')  
