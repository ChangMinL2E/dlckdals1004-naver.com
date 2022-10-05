# BOJ_1182 / Backtracking

def per(k,n,curSum,count):
    global total

    if k == n:
        if curSum == target and count:
            total += 1
        return

    per(k+1,n,curSum+Lst[k],count+1)
    per(k+1,n,curSum,count)

N, target = map(int,input().split())
Lst = list(map(int,input().split()))
total = 0

per(0,N,0,0)
print(total)