# bit = [0,0,0,0]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
# print(bit)

# arr = [3, 6, 7, 1, 5, 4]
#
# n = len(arr)
# # 1<<n, 2**n,
# for i in range(1 << n):  # 0~31 (000000~111111 < 1000000), 001001
#     for j in range(n):  # 0~5
#         check = 1 << j  # i의 각 bit 를 확인 000001 ~ 100000
#         if i & check:  # i = 1 , j = 0
#             print(arr[j], end=",")
#     print()
# print()

