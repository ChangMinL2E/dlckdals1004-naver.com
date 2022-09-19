# BOJ_11651 좌표 정렬

N = int(input())
lst = [tuple(map(int,input().split())) for _ in range(N)]
lst = sorted(lst, key= lambda x: (x[1],x[0]))

for ls in lst:
    print(*ls)