# 1225. 암호생성기

for tc in range(1,11):
    N = int(input())
    Q = list(map(int,input().split()))
    cml = True
    cnt = 0

    while cml:
        temp = 0
        Q[0] = Q[0] - (cnt % 5 + 1)
        temp = Q[0]
        for i in range(1,8):
            Q[i-1] = Q[i]
        Q[7] = temp
        cnt += 1

        if Q[7] <= 0:
            Q[7] = 0
            print(f'#{tc}',*Q)
            cml = False







