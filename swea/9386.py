# 9386. 연속한 1의 개수

T = int(input())

for tc in range(1,T+1):
    input()
    N = input()

    total = 0
    maximum = 0
    for s in N:
        if s == '1':
            total += 1
        else:
            total = 0

        if maximum < total:
            maximum = total
    print(f'#{tc} {maximum}')



