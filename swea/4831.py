# K, N, M
# K는 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N은 0번부터 종점 정류장 번호
# M은 충전기가 설치된 M개의 정류장 번호.

# T = 1
T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    lst = [0 for _ in range(N+1)] # lst = [0,0,0,...,0]
    N2 = map(int,input().split())
    for n2 in N2:
        lst[n2] = 1 # lst = [0,1,0,1,...] 충전기 존재하는 주유소.
    
    total = 0
    count = 0
    last = 0
    LEE = True
    while LEE:
        for ele in range(last+K,last,-1):
            if last+K >= N:
                LEE = False
                break
            elif lst[ele] == 1:
                last = ele
                count += 1
                break
            elif lst[last+1:last+K+1].count(1) == 0:
                count = 0
                LEE = False
                break
    
    print(f'#{tc} {count}')
