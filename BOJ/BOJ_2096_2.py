# BOJ_2096_2 내려가기 / 메모리 초과
# 읽고 버리자.
import copy, sys

input = sys.stdin.readline

N = int(input())
max_lst = list(map(int, input().split()))  # 첫줄만
min_lst = copy.deepcopy(max_lst)  # 읽자

while N - 1:
    This_lst1 = copy.deepcopy(max_lst)
    This_lst2 = copy.deepcopy(min_lst)
    a, b, c = map(int, input().split())

    max_lst[0] = a + max(This_lst1[0], This_lst1[1])
    max_lst[1] = b + max(This_lst1[0], This_lst1[1], This_lst1[2])
    max_lst[2] = c + max(This_lst1[2], This_lst1[1])

    min_lst[0] = a + min(This_lst2[0], This_lst2[1])
    min_lst[1] = b + min(This_lst2[0], This_lst2[1], This_lst2[2])
    min_lst[2] = c + min(This_lst2[2], This_lst2[1])

    N -= 1

print(max(max_lst), min(min_lst))
