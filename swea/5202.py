# 03 Greedy algorithm 화물 도크

# 종료 시간 기준 일찍 끝나는걸 넣겠다.

for tc in range(1,int(input())+1):
    N = int(input())
    Trucks = []
    for _ in range(N):
        Trucks.append(tuple(map(int,input().split())))

    Trucks.sort(key=lambda x:x[1]) # 끝나는 시간 기준 정렬
    maximum = 0
    lst = []
    visited = [False] * N
    total = 0

    while len(Trucks):
        if lst == []: # 첫번째 차부터 넣어보고, 경우 보고, 다음 차 경우보고, ...
            lst.append(Trucks.pop(0))
            total = 1
        else:
            for Truck in Trucks:
                if lst[-1][1]<=Truck[0]:
                    lst.append(Truck)
                    total += 1

            if total > maximum:
                maximum = total

            lst = []

    print(f'#{tc} {maximum}')