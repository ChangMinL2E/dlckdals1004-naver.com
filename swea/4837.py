# 원소의 개수 N개, 원소의 합 K 인 부분 집합 개수 찾기.
from itertools import combinations

T = int(input())
# T = 1

for tc in range(1, T + 1):
    A = [x for x in range(1, 13)]
    N, K = map(int, input().split())
    total = 0
    for jh in combinations(A, N):
        if sum(jh) == K:
            total += 1

    print(f'#{tc} {total}')

