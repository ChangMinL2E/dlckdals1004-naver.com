# BOJ_11399 ATM

N = int(input())
lst = sorted(list(map(int,input().split())))

total = 0
for i in range(N):
    total += lst[i]*(N-i)

print(total)