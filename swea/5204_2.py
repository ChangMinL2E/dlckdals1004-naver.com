# 4 병합정렬 - 병합 정렬
# 분할이랑 병합을 따로 함수 만들자.
# 런타임 에러 -> append 메소드를 사용하지 않았다. -> pass

def merge_sort(lst):  # 분할
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)  # 분할 계속 돌리다가 끝나면 병합하겠다.
    right = merge_sort(right)

    return merge(left, right)  # 병합.


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1  # cnt

    result = [0] * (len(left) + len(right))  # 인덱싱/ 슬라이싱 을 사용하기 위해.
    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result[result_idx] = left[left_idx]
            result_idx += 1
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]
            result_idx += 1
            right_idx += 1
    if left_idx < len(left):
        for ele in left[left_idx:]:
            result[result_idx] = ele
            result_idx += 1

    if right_idx < len(right):
        for ele in right[right_idx:]:
            result[result_idx] = ele
            result_idx += 1
    return result


for tc in range(1, int(input()) + 1):
    N = int(input())  # len(lst)
    Lst = list(map(int, input().split()))
    cnt = 0
    new_List = merge_sort(Lst)  # return 값을 받아줘야 한다.
    # print(new_List)

    print(f'#{tc} {new_List[N // 2]} {cnt}')
