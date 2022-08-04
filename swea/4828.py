T = int(input())
# T = 1

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    lst = sorted(lst)
    gap = abs(lst[0]-lst[N-1])

    print(f'#{tc} {gap}')