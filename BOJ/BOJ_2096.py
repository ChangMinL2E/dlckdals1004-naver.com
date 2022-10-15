# BOJ_2096 내려가기 / 메모리 초과
import copy, sys
input = sys.stdin.readline

N = int(input())
max_lst = [list(map(int,input().split())) for _ in range(N)]
min_lst = copy.deepcopy(max_lst)

k = 1
while N-k:
    max_lst[k][0] += max(max_lst[k-1][0],max_lst[k-1][1])
    max_lst[k][1] += max(max_lst[k-1][0],max_lst[k-1][1],max_lst[k-1][2])
    max_lst[k][2] += max(max_lst[k-1][2],max_lst[k-1][1])

    min_lst[k][0] += min(min_lst[k - 1][0], min_lst[k - 1][1])
    min_lst[k][1] += min(min_lst[k - 1][0], min_lst[k - 1][1], min_lst[k - 1][2])
    min_lst[k][2] += min(min_lst[k - 1][2], min_lst[k - 1][1])

    k+=1

print(max(max_lst[-1]),min(min_lst[-1]))
