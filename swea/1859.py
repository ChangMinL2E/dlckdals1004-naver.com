T = int(input())

for tc in range(T):
    N = int(input()) # len(lst)
    # N = 5
    cost = list(map(int,input().split()))

    # cost = [1,1,3,1,2]
    revenue = 0
    while cost != []:
        high_1 = max(cost)
        for i in range(len(cost)):
            i_1 = 0
            if cost[i] == high_1:
                i_1 = i
                break

        revenue += cost[i_1]*(i_1) - sum(cost[:i_1])
        for _ in range(i_1+1):
            del cost[0]


    print(f'#{tc+1} {revenue}')