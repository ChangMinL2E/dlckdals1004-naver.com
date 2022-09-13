# swea5207 4병합정렬 - 이진탐색
# B의 원소중 A의 원소에 몇개 있는지 확인하기.
# 1. A의 원소정렬 2. 양쪽구간 번갈아서 검색.

def binarySearch(lst, key):
    st = 0
    ed = len(lst) - 1
    direction = 0
    while st <= ed:
        middle = st + (ed - st) // 2
        if key == lst[middle]:
            return 1  # 찾으면 1을 더하겠다.
        if key < lst[middle]:
            if direction == -1:
                return 0
            else:
                ed = middle - 1
                direction = -1
        else:
            if direction == 1:
                return 0
            else:
                st = middle + 1
                direction = 1
    return 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    total = 0
    for b in B:
        total += binarySearch(A, b)

    print(f'#{tc} {total}')
