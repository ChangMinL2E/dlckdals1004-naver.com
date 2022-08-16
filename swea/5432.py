# 5432. 쇠막대기 자르기

def cut(Lst):
    total_cnt = 0
    for i in range(len(Lst)):  # 100,000이하
        cnt = 1
        if Lst[i] == ')':  # ) 이 나온다면,
            for j in range(i, -1, -1):
                if Lst[j] == '0':  # 사이의 빔의 개수를 찾아내겠다.
                    cnt += 1

                elif Lst[j] == '(':  # ( 짝을 찾고,
                    total_cnt += cnt
                    Lst[j] = 1
                    Lst[i] = 1
                    break

    return total_cnt


for tc in range(1, int(input()) + 1):
    N = input().split('()')
    N = '0'.join(N)
    lst = list(N)

    print(f'#{tc} {cut(lst)}')
