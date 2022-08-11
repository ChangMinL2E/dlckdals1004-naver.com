# 원소의 개수 N개, 원소의 합 K 인 부분 집합 개수 찾기.
# from itertools import combinations

T = int(input())
# T = 1

def sum2(lst):
    sum3 = 0
    for i in lst:
        sum3 += i
    return sum3

A = [x for x in range(1, 13)]
A_subset = []

n = len(A)

for i in range(1 << n):
    B = []
    for j in range(n):
        check = 1 << j
        if i & check:
            B.append(A[j])
    A_subset.append(B)
# print(A_subset)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    total = 0

    for subset in A_subset:
        if sum2(subset) == K and len(subset) == N:
            total += 1

    print(f'#{tc} {total}')
