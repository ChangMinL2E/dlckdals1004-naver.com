T = int(input())

for tc in range(1,T+1):
    N = int(input())

    def A(n):
        if (n == 1)or(n==2)or(n==3):
            return 1
        elif (n==4)or(n==5):
            return 2
        else:
            return A(n-1)+A(n-5)

    print(f'#{tc} {A(N)}')