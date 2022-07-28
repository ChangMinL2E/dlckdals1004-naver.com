# 1204 swea

# T = 10

T = int(input())
for _ in range(T):
# N = 1
    N = int(input())
    N2 = map(int,input().split())
    N2 = list(N2)
    new_N2 = list(set(N2))

    most_i = 0
    for i in range(101):
        if N2.count(i) >= N2.count(most_i):
            most_i = i

    print(f'#{N} {most_i}')