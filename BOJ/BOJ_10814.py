# BOJ_10814 나이순 정렬

N = int(input())
lst = [list(input().split()) for _ in range(N)]
for i in range(N):
    lst[i].append(i)

lst = sorted(lst, key=lambda x:(int(x[0]),x[2]))

for ls in lst:
    print(ls[0],ls[1])


