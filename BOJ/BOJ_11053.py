# BOJ_11053 증가 수열

N = int(input())
lst = list(map(int,input().split()))
count = [0]*N

for idx in range(len(lst)):
    for i in range(idx):
        if lst[idx] > lst[i] and count[idx] < count[i]:
            lst[i] = lst[idx]
    count[idx] += 1
print(max(count))









