# BOJ_11047 동전 0

# def Backtracking(k,curSum):
#     global minimum
#
#     if k > minimum:
#         return
#
#     if curSum == 0:
#         minimum = k
#         return
#
#     for ls in lst:
#         if curSum-ls>= 0:
#             Backtracking(k+1,curSum-ls)

N, K = map(int,input().split())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)
# minimum = 1e10

# Backtracking(0,K)
# print(minimum)
total = 0
i = 0
while K:
    if K - lst[i]>=0:
        total += K//lst[i]
        K %= lst[i]

    i += 1
print(total)
