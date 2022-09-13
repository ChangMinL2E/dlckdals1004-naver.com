# 05_Backtracking swea_5208 전기버스 2
# battery에서 에러가 있다

def Go(lst,k,n,battery,cnt):
    global minimum

    if k == n:
        minimum = cnt

    if cnt >= minimum or battery < 0:
        return

    if k != n-1:
        Go(lst, k+1, n, battery-1, cnt) # 충전 안할때
        Go(lst, k+1, n, lst[k], cnt+1) # 충전 할때
    else:
        if battery == 0:
            Go(lst, k+1, n, 0, cnt+1)
        else:
            Go(lst, k+1, n, 0, cnt)


for tc in range(1,int(input())+1):
    bus_lst = list(map(int,input().split()))

    N = bus_lst.pop(0)
    minimum = 1000000
    # print(bus_lst)
    Go(bus_lst,0,N-1,bus_lst[0],0)

    print(minimum)