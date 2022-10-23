# BOJ_11726 2xn 타일링

import sys
input = sys.stdin.readline
# 이런 함수.
# def A(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return A(n-2)+A(n-1)


N = int(input())
lst = [0,1,2]
# for i in range(3,1001):
#     lst.append(lst[i-1]+lst[i-2])
for i in range(3,N+1):
    lst.append(lst[i-1]+lst[i-2])

print(lst[N]%10007)
