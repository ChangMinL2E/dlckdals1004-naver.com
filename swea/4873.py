

T = int(input())

for tc in range(1,T+1):
    lst = []
    N = input()
    for st in N:
        if len(lst) == 0:
            lst.append(st)
        elif st == lst[-1]:
            lst.pop()
        else:
            lst.append(st)
    print(f'#{tc} {len(lst)}')