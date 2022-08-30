# BOJ_1026 보물

N = int(input())

A = sorted(list(map(int,input().split())), reverse=False)
B = sorted(list(map(int,input().split())), reverse=True)

total = 0

for i in range(N):
    total += A[i]*B[i]

print(total)
