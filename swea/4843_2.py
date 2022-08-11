# 특별한 정렬


T = int(input())
# T = 1
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


for tc in range(1,T+1):
    N = int(input())
    org = list(map(int,input().split()))
    bubble_sort(org) # 오름차순 정렬
    new_lst = []

    for i in range(5):
        new_lst.append(org[len(org)-i-1])
        new_lst.append(org[i])

    new_st = ''
    for j in new_lst:
        new_st += str(j)+' '

    print(f'#{tc} {new_st}')

