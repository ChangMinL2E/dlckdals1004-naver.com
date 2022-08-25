# 4047. 영준이의 카드 카운팅

for tc in range(1, int(input()) + 1):
    N = input()
    length = len(N)
    lst = [[0]*14 for _ in range(4)]

    for i in range(length // 3):
        card = N[3 * i:3 * i + 3]
        if card[0] == 'S':
            idx = int(card[1:])
            lst[0][idx] += 1
        elif card[0] == 'D':
            idx = int(card[1:])
            lst[1][idx] += 1
        elif card[0] == 'H':
            idx = int(card[1:])
            lst[2][idx] += 1
        elif card[0] == 'C':
            idx = int(card[1:])
            lst[3][idx] += 1

    out = ''

    for ls in lst:
        if ls.count(0) + ls.count(1) != 14:
            out = "ERROR"
            break
        else:
            out += str(13-sum(ls))+' '

    print(f'#{tc} {out}')
