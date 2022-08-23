# 1493 수의 새로운 연산
# 수정해라


# def S(n):
#     if memo[n] == -1:
#         memo[n] = S(n-1)+n
#     return memo[n]
memo = [-1] * 201
memo[0] = 0
for i in range(1, 201):
    memo[i] = int(((1 + i) / 2) * i)


# memo[1] = 1
# memo[2] = 3
# for i in range(201):
#     S(i)
def S2(cml):
    for j in range(len(memo)):
        if memo[j] >= cml:
            b = cml - memo[j - 1]
            a = j
            return (b, a - b + 1)


for tc in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    p1 = S2(p)
    q1 = S2(q)

    sol = (p1[0] + q1[0], p1[1] + q1[1])
    sol2 = memo[sol[0] + sol[1] - 2] + sol[0]

    print(f'#{tc} {sol2}')
