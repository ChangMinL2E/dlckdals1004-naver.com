# 5177. 이진 최소 힙
# 왜 오답?

from heapq import heapify


def parent_sum(lst, cnt):
    global total
    cnt //= 2
    if cnt == 1:
        total += lst[cnt]
        return
    else:
        total += lst[cnt]
        parent_sum(lst, cnt)


for tc in range(1, int(input()) + 1):
    # which = int(input())
    int(input())
    heap = list(map(int, input().split()))  # 부모 노드 인덱스를 사용하기 위해 0 추가.
    heapify(heap)

    heap.insert(0, 0)
    # print(heap)
    total = 0
    which = len(heap) - 1

    parent_sum(heap, which)
    print(f'#{tc} {total}')
