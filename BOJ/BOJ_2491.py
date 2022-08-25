# 2491. 수열

N = int(input())

maximum = 0
total = 1
conti = 0

lst = list(map(int, input().split()))
button = 1
if len(lst) == 1:
    maximum = 1
elif lst[0] > lst[1]:
    button = 0
elif lst[0] < lst[1]:
    button = 1

for i in range(1, N):
    if len(lst) == 1:
        maximum = 1
        break

    if lst[i - 1] < lst[i]:
        if button:
            total += 1
        else:
            button = 1
            total = 2 + conti
        conti = 0

    elif lst[i - 1] > lst[i]:
        if (i == 1) and lst[0] == lst[1]:  # 초기값 예외 처리
            button = 0
            total += 1
            conti = 1
        elif not button:
            total += 1
            conti = 0
        else:
            button = 0
            total = 2 + conti
            conti = 0

    else:  # lst[i-1] == lst[i]
        total += 1
        conti += 1

    if maximum < total:
        maximum = total

print(maximum)
