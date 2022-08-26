# 13976. IM 대비 기지국

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = []

    for _ in range(2):
        lst.append(['X'] * 9)
    for _ in range(10):
        lst.append(list(input()))
    for _ in range(2):
        lst.append(['X'] * 9)

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 'A':
                lst[i][j - 1: j + 2] = ['X', 'A', 'X']
                lst[i + 1][j] = 'X'
                lst[i - 1][j] = 'X'

            elif lst[i][j] == 'B':
                for l in [1, 2]:
                    lst[i + l][j] = 'X'
                    lst[i - l][j] = 'X'
                lst[i][j - 2:j + 3] = ['X', 'X', 'B', 'X', 'X']
            elif lst[i][j] == 'C':
                for z in [1, 2, 3]:
                    lst[i + z][j] = 'X'
                    lst[i - z][j] = 'X'
                lst[i][j - 3: j + 4] = ['X', 'X', 'X', 'C', 'X', 'X', 'X']

    total = 0
    for ls in lst:
        total += ls.count('H')

    print(f'#{tc} {total}')
