# 02 완전 검색 전자카트

# 고려사항은 마지막에 무조건 1로 가야한다는 1차원 백트래킹


def Backtracking(lst, cnt, k, N, curSum):
    global minimum

    if curSum > minimum:
        return

    # if cnt == N:
    #     if curSum < minimum:
    #         minimum = curSum
    #     return

    if cnt == N-1:
        curSum += lst[k][0]
        if curSum < minimum:
            minimum = curSum
        return

    else:
        for i in range(1,N):
            if not visited[i]: #and (i != k): # 똑같은곳으로 가는건 시간낭비, k -> i 인 함수를 짠다.
                visited[i] = True
                Backtracking(lst, cnt+1, i, N, curSum+lst[k][i])
                visited[i] = False

for tc in range(1, int(input())+1):
    N = int(input())
    minimum = 10**8
    visited = [False]*N
    Matrix = []
    for _ in range(N):
        Matrix.append(list(map(int,input().split())))

    Backtracking(Matrix,0,0,N,0)
    print(f'#{tc} {minimum}')











