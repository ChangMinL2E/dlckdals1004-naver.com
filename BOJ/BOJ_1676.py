# BOJ_1676 Factorial

lst = [0]*501
lst[0] = 1
for i in range(1,501):
    lst[i] = lst[i-1]*i

def cnt(num):
    target = str(lst[num])
    cnt2 = 0
    for t in target[::-1]:
        if t == '0':
            cnt2 += 1
        else:
            break

    print(cnt2)
    return

cnt(int(input()))



