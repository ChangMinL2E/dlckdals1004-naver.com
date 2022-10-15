# BOJ_11660_2 구간합은 합 list를 만들어서 풀어야 하나..?
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

Lst = [list(map(int,input().split())) for _ in range(N)]
plus_lst = [0]*(N**2+1)

for i in range(N*N):
    plus_lst[i+1] = plus_lst[i]+Lst[i//N][i%N]

for _ in range(M):
    st_row, st_col, ed_row, ed_col = map(int,input().split())
    st_row, st_col, ed_row, ed_col = st_row-1, st_col-1, ed_row-1, ed_col-1
    total = 0

    for row_i in range(st_row, ed_row+1):
        total += plus_lst[row_i * N + ed_col + 1] - plus_lst[row_i * N + st_col]

    print(total)







