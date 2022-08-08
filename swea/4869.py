def A(n):
    if n%2 == 1: # 홀수
        if n == 1: # 1
            return 1
        else: # 4배하고 1더해서 주세요.
            return 4*A(n-2)+1
    else: # 짝수
        if n == 2:
            return 3
        else: # 4배하고 1빼서 주세요.
            return 4*A(n-2)-1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    
    print(f'#{tc} {A(N/10)}')

# print(A(4))
