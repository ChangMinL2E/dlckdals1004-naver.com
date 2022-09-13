# 4 병합정렬 - 퀵 정렬
# 재귀 함수의 quicksort와 pivot index를 반환해주는 partition을 만들자.

def quickSort(lst,st,ed):
    if st< ed:
        pivot_idx = partition(lst,st,ed)
        quickSort(lst,st,pivot_idx-1)
        quickSort(lst,pivot_idx+1,ed)
    # return 값이 없다. 결국 lst를 그대로 정렬해준다.

def partition(lst,st,ed):
    pivot = lst[st]
    i = st+1 # pivot 다음 index가 출발
    j = ed # 마지막부터 index 출발

    while i <= j:
        while i<=j and lst[i] <= pivot: # pivot보다 작으면 넘어가겠다.
            i += 1
        while i<=j and lst[j] >= pivot: # pivot보다 크면
            j -= 1
        if i <= j: # pivot보다 작은, 큰 원소의 위치를 바꿔주겠다.
            lst[i],lst[j] = lst[j],lst[i]
    lst[st],lst[j] = lst[j],lst[st]
    return j # 인덱스를 반환




for tc in range(1,int(input())+1):
    N = int(input())
    Lst = list(map(int,input().split()))
    quickSort(Lst,0,N-1)

    print(f'#{tc} {Lst[N//2]}')







