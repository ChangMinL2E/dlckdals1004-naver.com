# BOJ_1912 연속합

import sys
input = sys.stdin.readline

N = int(input())
Lst = list(map(int, input().split()))
lst = [Lst[0]]
for i in range(len(Lst) - 1):
    lst.append(max(lst[i] + Lst[i + 1], Lst[i + 1]))
print(max(lst))