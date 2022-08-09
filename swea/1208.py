# 덤프 횟수 후에 최고점과 최저점의 높이 차이 구하기.
import sys

sys.stdin = open('1208.txt')


def maxV(lst):
    ls = lst[0]
    for i in range(len(lst)):
        if lst[i] > ls:
            ls = lst[i]
    return ls

def minV(lst):
    ls = lst[0]
    for i in range(len(lst)):
        if ls > lst[i]:
            ls = lst[i]
    return ls

for tc in range(1,11):
    N = int(input())
    lst = list(map(int,input().split()))

    for _ in range(N):
        k = 0
        l = 0
        for i in range(len(lst)):
            if maxV(lst) == lst[i]:
                k = i
            elif minV(lst) == lst[i]:
                l = i

        if lst[k] - lst[l] > 2:
            lst[k] -= 1
            lst[l] += 1

    print(f'#{tc} {maxV(lst)-minV(lst)}')