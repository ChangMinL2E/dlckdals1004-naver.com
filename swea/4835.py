# 총 개수 N개의 배열, M개의 원소 합중 최대 최소 차이.

T = int(input())
# T = 1

for tc in range(1,T+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    high = 0
    low = sum(lst[0:M])

    for i in range(N-M+1):
        score = sum(lst[i:i+M])
        if score > high:
            high = score
        elif score < low:
            low = score
    
    print(f'#{tc} {high-low}')