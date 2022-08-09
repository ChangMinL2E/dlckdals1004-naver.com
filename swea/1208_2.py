# 덤프 횟수 후에 최고점과 최저점의 높이 차이 구하기.
# 개선점.
# 1. 출발점을 바꿀것. 0,100 -> min, max로 바꿀것.
# 2. for문을 돌릴때, 좀 더 획기적인 방법을 사용해볼것.
import sys

sys.stdin = open('1208.txt')

for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt_lst = [0] * (100 + 1)
    for ls in lst:
        cnt_lst[ls] += 1

    low_num = 0
    high_num = 0
    low_cnt = 0
    high_cnt = 0
    i1 = 0
    i2 = 100

    while low_num <= N:
        cnt_lst[i1 + 1] += cnt_lst[i1]
        low_num += cnt_lst[i1]
        i1 += 1

    while high_num <= N:
        cnt_lst[i2 - 1] += cnt_lst[i2]
        high_num += cnt_lst[i2]
        i2 -= 1

    if low_num > N:
        low_cnt = i1 - 1
    else:
        low_cnt = i1

    if high_num > N:
        high_cnt = i2 + 1
    else:
        low_cnt = i2
    print(f'#{tc} {high_cnt - low_cnt}')
