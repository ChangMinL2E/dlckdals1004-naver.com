# 이진수2

for tc in range(1,int(input())+1):
    num = float(input())
    cnt = -1
    S = ''
    while num!=0 and cnt > -14:
        a = int(num // (2**cnt))
        num = num % (2**cnt)
        S = S + str(a)
        cnt -= 1

    if len(S)>= 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {S}')





