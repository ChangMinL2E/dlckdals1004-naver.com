# 1289. 원재의 메모리 복구하기.

for tc in range(1,int(input())+1): # test case
    bits = input()

    default = '0'
    cnt = 0

    for bit in bits:
        if default != bit:
            default = bit
            cnt += 1

    print(f'#{tc} {cnt}')

