# BOJ_2579 계단 오르기

def per(k,N,jump,curSum):
    global maximum
    if k >= N:
        if maximum < curSum:
            maximum = curSum
        return

    if jump == 2:
        per(k+1,N,1,curSum+Lst[k+1])
        per(k+2,N,2,curSum+Lst[k+2])
    else:
        per(k+2,N,2,curSum+Lst[k+2])

N = int(input())
Lst = [int(input()) for _ in range(N)]
Lst.append(0)
Lst.append(0)
maximum = 0

per(0,N-1,2,Lst[0])

print(maximum)
