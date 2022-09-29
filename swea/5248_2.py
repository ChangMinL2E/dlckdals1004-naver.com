# 5248 그룹나누기
def find_set(x):
    while x!= Lst[x]:
        x = Lst[x]
    return x


for tc in range(1,int(input())+1):
    N, M = map(int,input().split())

    Lst = [i for i in range(N+1)]

    lst = list(map(int,input().split()))

    for i in range(M):
        n1 = find_set(lst[i*2])
        n2 = find_set(lst[i*2+1])
        Lst[n2] = n1

    count = 0
    for i in range(1,N+1):
        if i == Lst[i]:
            count += 1

    print(f'#{tc} {count}')


