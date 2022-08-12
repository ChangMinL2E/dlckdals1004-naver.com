import sys
sys.stdin = open('4881.txt')

T = int(input())

def backtrack(lst, sum, k):
    global min_sum

    if min_sum < sum:
        return
    if len(lst) == len(arr):
        min_sum = sum
        return

    for i in range(len(arr)):
        if i not in lst:
            backtrack(lst + [i], sum + arr[k + 1][i], k + 1)

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 100000000000
    for k in range(N):
        backtrack([k], arr[0][k], 0)
    print(f'#{tc} {min_sum}')
