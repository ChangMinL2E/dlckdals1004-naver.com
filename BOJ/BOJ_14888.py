# BOJ_14888 연산자 끼워넣기 / 백트래킹

def per(k,N,curSum):
    global maximum, minimum

    if k==N:
        if maximum < curSum:
            maximum = curSum
        if minimum > curSum:
            minimum = curSum
        return

    for i in range(4):
        if i == 0 and ope_dic[i]:
            ope_dic[i] -= 1
            per(k+1, N, curSum+Lst[k])
            ope_dic[i] += 1

        elif i == 1 and ope_dic[i]:
            ope_dic[i] -= 1
            per(k+1, N, curSum-Lst[k])
            ope_dic[i] += 1

        elif i == 2 and ope_dic[i]:
            ope_dic[i] -= 1
            per(k+1, N, curSum*Lst[k])
            ope_dic[i] += 1

        if i == 3 and ope_dic[i]:
            ope_dic[i] -= 1
            if curSum < 0:
                number = curSum
                number = -(abs(number)//Lst[k])
            else:
                number = curSum
                number = abs(number // Lst[k])
            per(k+1, N, number)
            ope_dic[i] += 1


N = int(input())
Lst = list(map(int,input().split()))
operations = list(map(int,input().split()))
ope_dic = {}
for idx in range(len(operations)):
    ope_dic[idx] = operations[idx]

minimum = 1e10
maximum = -1e10

for i in range(4):
    if i == 0 and ope_dic[i]:
        ope_dic[i] -= 1
        per(2, N, Lst[0]+Lst[1])
        ope_dic[i] += 1

    elif i == 1 and ope_dic[i]:
        ope_dic[i] -= 1
        per(2, N, Lst[0]-Lst[1])
        ope_dic[i] += 1

    elif i == 2 and ope_dic[i]:
        ope_dic[i] -= 1
        per(2, N, Lst[0]*Lst[1])
        ope_dic[i] += 1

    if i == 3 and ope_dic[i]:
        ope_dic[i] -= 1
        per(2, N, Lst[0]//Lst[1])
        ope_dic[i] += 1

print(maximum)
print(minimum)



