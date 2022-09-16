# swea 5688 세제곱근을 찾아라

def find_T(x):
    if abs(x**(1/3)- round(x**(1/3)))<1e-7:
        return round(x**(1/3))
    else:
        return -1

for tc in range(1,int(input())+1):
    print(f'#{tc} {find_T(int(input()))}')




