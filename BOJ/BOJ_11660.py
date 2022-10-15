# BOJ_11660 구간

N,M = map(int,input().split())

Lst = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    st_row, st_col, ed_row, ed_col = map(int,input().split())
    st_row, st_col, ed_row, ed_col = st_row-1, st_col-1, ed_row-1, ed_col-1
    total = 0

    for i in range(st_row,ed_row+1):
        total += sum(Lst[i][st_col:ed_col+1])

    print(total)


