T = int(input())
# T = 1

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    # lst = sorted(lst)
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[n-j-1] > lst[n-j-2]:
                lst[n-j-1], lst[n-j-2] = lst[n-j-2], lst[n-j-1]


    gap = lst[0]-lst[N-1]

    print(f'#{tc} {gap}')