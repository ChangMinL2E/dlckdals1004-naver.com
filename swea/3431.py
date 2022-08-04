# 준환이의 운동관리

# T = 1
T = int(input())

for tc in range(1,T+1):
    a,b,c = list(map(int,input().split()))

    if c < a:
        print(f'#{tc} {a-c}')
    elif a <= c <= b:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} -1')





