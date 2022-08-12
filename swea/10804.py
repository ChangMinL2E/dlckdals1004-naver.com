# 문자열의 거울상

T = int(input())

for tc in range(1,T+1):
    N = input()
    s = ''
    N_lst = [n for n in N]

    for i in range(len(N_lst)//2):
        N_lst[i], N_lst[len(N_lst)-i-1] = N_lst[len(N_lst)-i-1], N_lst[i]

    for i in range(len(N_lst)):
        if ord(N_lst[i]) < 100:
            N_lst[i] = chr(100)
        elif ord(N_lst[i])% 100 == 0:
            N_lst[i] = chr(98)
        elif ord(N_lst[i]) == 112:
            N_lst[i] = chr(ord(N_lst[i])+1)
        else:
            N_lst[i] = chr(ord(N_lst[i])-1)

    print(f"#{tc} {''.join(N_lst)}")



