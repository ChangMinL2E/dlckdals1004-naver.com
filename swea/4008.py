# 4008 숫자 만들기

def per(k,N,curSum):
    global minimum,maximum

    if k == N:
        if curSum > maximum:
            maximum = curSum
        if curSum < minimum:
            minimum = curSum
        return

    for idx in range(4):
        if cal_dic[idx] != 0:
            if idx == 0:
                curSum += Lst[k]
                cal_dic[idx] -= 1
                per(k+1,N,curSum)
                cal_dic[idx] += 1
                curSum -= Lst[k]
            elif idx == 1:
                curSum -= Lst[k]
                cal_dic[idx] -= 1
                per(k + 1, N, curSum)
                cal_dic[idx] += 1
                curSum += Lst[k]
            elif idx == 2:
                curSum *= Lst[k]
                cal_dic[idx] -= 1
                per(k + 1, N, curSum)
                cal_dic[idx] += 1
                curSum /= Lst[k]
            else: # idx == 3:
                if curSum < 0:
                    curSum = -(abs(curSum)//Lst[k])
                else:
                    curSum //= Lst[k]
                cal_dic[idx] -= 1
                per(k + 1, N, curSum)
                cal_dic[idx] += 1
                curSum *= Lst[k]


for tc in range(1,int(input())+1):
    N = int(input())
    minimum = 1e10
    maximum = -1e10
    cal_lst = list(map(int,input().split()))
    Lst = list(map(int,input().split()))

    cal_dic = {}
    for i in range(4):
        cal_dic[i] = cal_lst[i]

    for j in range(4):
        if cal_dic[j] != 0:
            if j == 0:
                cal_dic[j] -= 1
                per(2,N,Lst[0]+Lst[1])
                cal_dic[j] += 1

            elif j == 1:
                cal_dic[j] -= 1
                per(2, N, Lst[0] - Lst[1])
                cal_dic[j] += 1
            elif j == 2:
                cal_dic[j] -= 1
                per(2, N, Lst[0] * Lst[1])
                cal_dic[j] += 1
            else: # idx == 3:
                cal_dic[j] -= 1
                per(2, N, Lst[0] // Lst[1])
                cal_dic[j] += 1

    print(minimum)
    print(maximum)

    print(f'#{tc} {round(maximum-minimum)}')





