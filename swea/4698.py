# 테네스의 체

primes = [False, False] + [True] * 1000000


def generation(A, B):
    for num in range(2, B + 1):
        if primes[num]:
            for idx in range(num+num, B+1, num):
                primes[idx] = False

    # for j in range(2, int(num ** 0.5) + 1):
    #     if num % j == 0:
    #         break
    # else:
    #     primes[num] = True


for tc in range(1, int(input()) + 1):
    D, A, B = map(int, input().split())
    generation(A, B)
    # print(primes[A:B + 1])
    cnt = 0
    for idx in range(A, B+1):
        if primes[idx] and str(D) in str(idx):
            cnt += 1
    print(f'#{tc} {cnt}')
