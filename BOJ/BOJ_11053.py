# BOJ_11053 증가 수열
# 이 문제도 냅색

N = int(input())
lst = list(map(int,input().split()))
count = [0]*N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            count[i] = max(count[i],count[j])
    count[i] += 1

print(max(count))









