T = int(input())
# T  = 1

for tc in range(T):
    N = int(input())
    # N = 2
    speed = 0
    distance = 0
    for i in range(N):
        N2 = input()
        if N2 == '0':
            distance += speed
        else:
            N2 = list(map(int,N2.split()))
            if N2[0] == 1:
                speed += N2[1]
                distance += speed
            elif N2[0] == 2:
                if (speed-N2[1]) > 0:
                    speed -= N2[1]
                    distance += speed
                else:
                    speed = 0
    print(f'#{tc+1} {distance}')









