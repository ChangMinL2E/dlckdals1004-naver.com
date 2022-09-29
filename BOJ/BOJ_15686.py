# BOJ_15656 치킨 배달

def distance(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])


N, M = map(int,input().split())

Lst = []
for _ in range(N):
    Lst.append(list(map(int,input().split())))

CK_lst = []
Homes = []

minimum = 1e10

live_lst = []

for i in range(N):
    for j in range(N):
        if Lst[i][j] == 1:
            Homes.append((i,j))
        elif Lst[i][j] == 2:
            CK_lst.append((i,j))

def Backtracking(lst, st_id, k):
    global minimum
    if k == M:
        total = 0
        for home in Homes:
            plus_dis = 10000
            for ls in lst:
                if plus_dis > distance(ls,home):
                    plus_dis = distance(ls,home)
            total += plus_dis

            if minimum < total:
                return

        if minimum > total:
            minimum = total
            return

    else:
        for idx in range(st_id+1,len(CK_lst)-(M-len(lst)-1)):
            lst.append(CK_lst[idx])
            Backtracking(lst, idx, k+1)
            lst.pop(-1)

for num in range(len(CK_lst)-(M-1)):
    Backtracking([CK_lst[num]],num,1)


print(minimum)