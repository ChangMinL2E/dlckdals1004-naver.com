# BOJ_2559 수열

N, j = map(int,input().split())

lst = list(map(int,input().split()))

total = sum(lst[0:j]) # sum은 한 번만 구하자.
maximum = total
for i in range(1,N-j+1):
    total = total - lst[i-1] + lst[i+j-1]
    if maximum < total:
        maximum = total
print(maximum)
