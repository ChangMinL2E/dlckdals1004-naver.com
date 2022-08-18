# 1959. 두 개의 숫자열

for tc in range(1, int(input())+1):
    N1, N2 = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N1 > N2: # 작은것을 N1, A로 놓고 풀겠습니다.
        N1, N2 = N2, N1
        A, B = B, A

    maximum = 0
    for j in range(N2-N1+1): # 처음부터 맞춰서 마지막 맞을때까지 하겠습니다.
        # B1 = B[:] # 복사본
        total = 0
        for i in range(N1):
            total += B[i+j] * A[i]
            # B1[i+j] *= A[i] # 각 원소를 곱하고,
        #
        #
        # for b1 in B1[j:j+N1+1]:
        #     total += b1 # 곱한 원소를 모두 더해주겠습니다.

        if maximum < total:
            maximum = total

    print(f'#{tc} {maximum}')

