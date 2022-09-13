# 4 병합정렬 - 병합 정렬
# 분할이랑 병합을 따로 함수 만들자.
# 런타임 에러

def merge_sort(lst): # 분할
    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left) # 분할 계속 돌리다가 끝나면 병합하겠다.
    right = merge_sort(right)

    return merge(left, right)  # 병합.

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1 # cnt

    result = [] # 반환할 list

    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result


for tc in range(1,int(input())+1):
    N = int(input()) # len(lst)
    Lst = list(map(int,input().split()))
    cnt = 0
    new_List = merge_sort(Lst) # return 값을 받아줘야 한다.
    # print(new_List)

    print(f'#{tc} {new_List[N//2]} {cnt}')




