# BOJ_2839 설탕 배달

N = int(input())

cnt = 0
while True:
    if N < 0:
        print(-1)
        break

    if N%5 == 0:
        print(cnt+N//5)
        break

    N = N - 3
    cnt += 1