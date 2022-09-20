# BOJ_11653 소인수분해

N = int(input())

while N != 1:
    for i in range(2,N+1):
        if not N%i:
            print(i)
            N = N//i
            break


