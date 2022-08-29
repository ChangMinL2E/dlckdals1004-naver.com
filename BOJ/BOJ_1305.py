# BOJ_1305 광고
# Runtime error

N = int(input())
inputS = input()
stop = False

i = 0
# while
while i < N:
    Str = inputS[:]
    cml = True
    sol = inputS[N-i-1:]

    N_sol = len(sol) # 뒤에서부터 원소별로 비교하는데, 크기.
    Str = Str[:-N_sol] # 원소 빼고,
    cnt = len(Str)// N_sol

    while cml:
        if len(Str) <= N_sol:
            if Str == sol[-len(Str):] or Str == '':
                stop = True
            cml = False

        else:
            if Str[-N_sol*cnt:] == sol*cnt:
                Str = Str[:-N_sol*cnt]
            else:
                cml = False
        # else:
        #     if Str[-N_sol:] == sol:
        #         Str = Str[:-N_sol]
        #     else:
        #         cml = False

    if stop:
        print(i+1)
        break

    i = i+1

# for문

# for i in range(N):
#     Str = inputS[:]
#     cml = True
#     sol = inputS[N-i-1:]
#
#     N_sol = len(sol) # 뒤에서부터 원소별로 비교하는데, 크기.
#     Str = Str[:-N_sol] # 원소 빼고,
#     cnt = len(Str)// N_sol
#
#     while cml:
#         if len(Str) <= N_sol:
#             if Str == sol[-len(Str):] or Str == '':
#                 stop = True
#             cml = False
#
#         else:
#             if Str[-N_sol*cnt:] == sol*cnt:
#                 Str = Str[:-N_sol*cnt]
#             else:
#                 cml = False
#         # else:
#         #     if Str[-N_sol:] == sol:
#         #         Str = Str[:-N_sol]
#         #     else:
#         #         cml = False
#
#     if stop:
#         print(i+1)
#         break

