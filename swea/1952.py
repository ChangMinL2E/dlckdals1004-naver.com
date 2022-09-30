# 1952 수영장

def Backtracking(k,N,money):
    global minimum

    if money >= minimum:
        return

    if k >= N:
        minimum = money
        return

    if schedule[k] != 0:
        for idx in range(4):
            if idx == 0:
                Backtracking(k+1,N, money+payments[0]*schedule[k])
            elif idx == 1:
                Backtracking(k+1,N, money+payments[1])
            elif idx == 2:
                Backtracking(k+3, N, money+payments[2])
            else: # idx == 3:
                Backtracking(N,N,money+payments[3])
    else:
        Backtracking(k+1,N,money)

for tc in range(1,int(input())+1):
    payments = list(map(int,input().split()))
    schedule = list(map(int,input().split()))
    minimum = 1e10

    Backtracking(0,12,0)

    print(f'#{tc} {minimum}')









