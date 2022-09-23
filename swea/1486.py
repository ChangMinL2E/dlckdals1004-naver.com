# 1486 장훈이의 높은 선반

def Backtracking(lst, k, N, curSum):
    global minimum, B

    if curSum - B >= minimum:
        return

    if k == N:
        if 0 <= curSum - B < minimum:
            minimum = curSum - B
        return

    for idx in range(2):
        if idx == 0:
            Backtracking(lst, k + 1, N, curSum)
        else:
            Backtracking(lst, k + 1, N, curSum + H[k])


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    minimum = 1e+10

    for i in range(N):
        if i == 0:
            Backtracking(H, 1, N, 0)
        else:
            Backtracking(H, 1, N, H[0])

    print(f'#{tc} {minimum}')
