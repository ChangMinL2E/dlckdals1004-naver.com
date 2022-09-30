# BOJ_1654 랜선 자르기
# 다시 풀어.
import sys


N, M = map(int,sys.stdin.readline().split())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)
# for num in range(sum(lst)//M,0,-1):
#     total = 0
#     for ls in lst:
#         total += ls//num
#
#     if total == M:
#         print(num)
#         break

def mo(num):
    total = 0
    for ls in lst:
        total += ls//num
    return total

cml = True
cml2 = True
left = 0
right = sum(lst)//M
while cml:
    middle = (left+right)//2
    if mo(middle) >= M:
        left = middle
    else: # mo(middle) < M:
        right = middle

    if left == right-1:
        print(left)
        cml= False
    # else:
    #     left = middle
    #     right = left + 1
    #
    #     while cml2:
    #         if mo(left) != mo(right):
    #             print(left)
    #             cml = False
    #             cml2 = False
    #         else:
    #             left += 1
    #             right += 1



