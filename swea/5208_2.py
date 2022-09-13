# 05_Backtracking swea_5208 전기버스 2_2
# idea를 전기버스 1처럼 하자.


def Go(lst, idx, cnt):
    global minimum

    if minimum < cnt:
        return

    if idx >= N:
        minimum = cnt
        return

    for i in range(idx+lst[idx], idx, -1):
        Go(lst, i, cnt+1)


for tc in range(1,int(input())+1):
    bus_lst = list(map(int,input().split()))

    N = bus_lst.pop(0)-1 # 0->N-1 로 간다.
    minimum = 1000000000
    Go(bus_lst, 0, -1)

    print(f'#{tc} {minimum}')

