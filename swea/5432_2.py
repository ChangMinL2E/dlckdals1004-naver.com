# 5432. 쇠막대기 자르기

def cut(Lst):
    total_cnt = 0
    opn = 0

    for ls in Lst:
        if ls == '(':
            opn += 1
        elif ls == ')':
            opn -= 1
            total_cnt += 1
        else: # ls == '0
            total_cnt += opn

    return total_cnt


for tc in range(1, int(input()) + 1):
    N = input().split('()')
    N = '0'.join(N)
    lst = list(N)

    print(f'#{tc} {cut(lst)}')
