# BOJ_10816 숫자 카드 2

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
N1 = int(input())
Lst = list(map(int,input().split()))
count_lst = [0]*20000001
for ls in lst:
    count_lst[ls] += 1

for Ls in Lst:
    print(count_lst[Ls], end=' ')