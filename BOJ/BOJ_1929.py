# BOJ_1929 소수 구하기
import sys

M, N = map(int,sys.stdin.readline().split())

lst = []
for num in range(M, N+1):
    if num == 1:
        continue
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                break
        else:
            lst.append(num)
for ls in lst:
    print(ls)




