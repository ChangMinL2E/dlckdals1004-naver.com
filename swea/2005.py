# 2005. 파스칼의 삼각형

def tri(n):
    global memo
    if memo[n - 1] == []:
        for i in range(0, n):
            if i == 0 or i == n - 1:
                memo[n - 1].append(1)
            else:
                memo[n - 1].append(memo[n - 2][i - 1] + memo[n - 2][i])

    return memo[n - 1]

memo = [[] for _ in range(10)]
for tc in range(1, int(input()) + 1):

    N = int(input())
    print(f'#{tc}')
    for i in range(1, N+1):
        A = tri(i)
        print(*A)