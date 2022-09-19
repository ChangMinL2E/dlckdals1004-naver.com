# BOJ_2750  수 정렬하기

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

for ls in lst:
    print(ls)


