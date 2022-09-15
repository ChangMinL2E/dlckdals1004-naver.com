N,K,M = map(int,input().split())

total = 1
for num in range(N-K+1,N+1):
    total *= num

for num2 in range(1,K+1):
    total //= num2

print(total%M)