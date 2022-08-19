# # 4408. 음주가무 후 방으로 돌아가기
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     lst = [[]]
#
#     for _ in range(N):
#         tu = tuple(map(int, input().split()))
#         a, b = tu[0], tu[1]
#         if a > b:
#             a, b = b, a
#
#         cnt = 0
#         cml = True
#         test_lst = []
#         test_lst = [x for x in range(a, b + 1)]
#         while cml:  # 넣을 순서(cnt) 정하기.
#             cml2 = True
#             while cml2:
#                 for t in test_lst:
#                     if cnt == len(lst):
#                         lst.append([])
#                         cml = False
#                         cml2 = False
#
#                     elif t in lst[cnt]:
#                         cnt += 1
#                         cml2 = False
#
#                     elif t == test_lst[0]:
#                         if t % 2 == 0 and t - 1 in lst[cnt]:
#                             cnt += 1
#                             cml2 = False
#                         elif t + 1 in lst[cnt]:
#                             cnt += 1
#                             cml2 = False
#
#                     elif t == test_lst[-1]:
#                         if t % 2 == 0 and t - 1 in lst[cnt]:
#                             cnt += 1
#                             cml2 = False
#                         elif t + 1 in lst[cnt]:
#                             cnt += 1
#                             cml2 = False
#
#                         else:
#                             cml = False
#                             cml2 = False
#
#         for item in test_lst:
#             lst[cnt].append(item)
#
#     print(lst)
#     print(f'#{tc} {len(lst)}')

# 4408. 음주가무 후 방으로 돌아가기

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [[]]

    for _ in range(N):
        tu = tuple(map(int, input().split()))
        a, b = tu[0], tu[1]
        if a > b:
            a, b = b, a

        if a%2 == 0:
            a = a-1

        if b%2 == 1:
            b = b+1

        print(a,b)

        cnt = 0
        cml = True
        test_lst = []
        test_lst = [x for x in range(a, b + 1)]
        while cml:  # 넣을 순서(cnt) 정하기.
            cml2 = True
            while cml2:
                for t in test_lst:
                    if cnt == len(lst):
                        lst.append([])
                        cml = False
                        cml2 = False

                    elif t in lst[cnt]:
                        cnt += 1
                        cml2 = False

                    elif t == test_lst[-1]:
                        cml = False
                        cml2 = False

        for item in test_lst:
            lst[cnt].append(item)

        print(lst)

    print(f'#{tc} {len(lst)}')
