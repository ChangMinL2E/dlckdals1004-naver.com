# swea 5185 이진수

for tc in range(1,(int(input()))+1):
    N, Input16 = input().split()
    N = int(N)
    S = ''

    total = 0
    dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

    for i in range(N-1,-1,-1):
        if 65<= ord(Input16[i]) <= 70:
            num = dic[Input16[i]]
            plus_S = ''
            lst = [0, 0, 0, 0]
            cnt = 3
            while num:
                a = num % 2
                lst[cnt] = a
                num //= 2
                cnt -= 1

        else:
            num = int(Input16[i])
            plus_S = ''
            lst = [0, 0, 0, 0]
            cnt = 3
            while num:
                a = num % 2
                lst[cnt] = a
                num //= 2
                cnt -= 1

        lst = map(str,lst)
        plus_S = ''.join(lst)
        S = plus_S + S
    print(f'#{tc} {S}')
