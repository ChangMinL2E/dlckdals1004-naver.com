# binary Search

def binary_search(key):
    st = 0
    ed = N - 1
    total = 0
    while st <= ed:
        total += 1
        m = (st + ed) // 2
        if lst[m] == key:  # 찾은 경우
            return total
        elif lst[m] < key:  # 앞의 내용을 버릴경우,
            st = m
        else:
            ed = m


T = int(input())

for tc in range(1,T+1):
    N, F1, F2 = map(int,input().split())
    lst = [i for i in range(1,N+1)]
    F1_cnt = binary_search(F1)
    F2_cnt = binary_search(F2)

    if F1_cnt < F2_cnt:
        print(f'#{tc} A')
    elif F1_cnt > F2_cnt:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')

