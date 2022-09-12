# 03_Greedy algorithm 컨테이너 운반
# idea. 큰 컨테이너부터 공간이 많이 남는순으로 넣어주겠다. 아 트럭당 컨테이너 하나 밖에 못넣는다.

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    Containers = sorted(list(map(int,input().split())), reverse=True)
    Trucks = sorted(list(map(int,input().split())), reverse=True)
    # Trucks = list(map(int,input().split()))
    total = 0

    for Container in Containers:
        # Trucks.sort(reverse=True) # 계속 정렬
        if len(Trucks) == 0:
            break

        elif Container <= Trucks[0]:
            total += Container
            Trucks.pop(0)

    print(f'#{tc} {total}')





