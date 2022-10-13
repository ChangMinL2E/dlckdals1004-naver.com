# BOJ_2407 조합

N,M = map(int,input().split())

def fac(r):
    if r == 0:
        return 1
    return fac(r-1)*r

print(round(fac(N)//(fac(N-M)*fac(M)))) # why?








