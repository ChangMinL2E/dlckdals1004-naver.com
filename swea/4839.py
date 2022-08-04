# 이진탐색

T = int(input())
# T = 1

for tc in range(1,T+1):
    C, A, B = map(int,input().split())

    def con(num, C):
        count = 0
        cml = True
        l = 1
        r = C
        while cml:
            c = int((l+r)/2)
            if c == num:
                count += 1
                cml = False
            else:
                count += 1
                if c > num:
                    r = c
                else:
                    l = c
        return count

    if con(A,C) > con(B,C):
        print(f'#{tc} B')
    if con(A,C) < con(B,C):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')

