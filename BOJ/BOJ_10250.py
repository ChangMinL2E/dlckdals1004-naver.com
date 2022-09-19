# BOJ_10250 ACM 호텔

for tc in range(int(input())):
    H, W, N = map(int,input().split())
    if N%H == 0:
        height = H
    else:
        height = N%H
    if N <= H*9:
        if N%H == 0:
            print(f'{height}0{N//H}')
        else:
            print(f'{height}0{N//H+1}')
    else:
        if N % H == 0:
            print(f'{height}{N // H}')
        else:
            print(f'{height}{N // H + 1}')




