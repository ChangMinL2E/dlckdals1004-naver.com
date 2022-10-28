# BOJ_15658 연산자 끼워넣기

import sys
input = sys.stdin.readline

def recursion(k,N,curSum):
    global maximum, minimum

    if k == N:
        if curSum > maximum:
            maximum = curSum
        if curSum < minimum:
            minimum = curSum
        return

    for i in range(4):
        if not i and dic[i]:
            dic[i] -= 1
            recursion(k+1,N,curSum+Lst[k])
            dic[i] += 1
        elif i == 1 and dic[i]:
            dic[i] -= 1
            recursion(k+1,N,curSum-Lst[k])
            dic[i] += 1
        elif i == 2 and dic[i]:
            dic[i] -= 1
            recursion(k+1,N,curSum*Lst[k])
            dic[i] += 1
        elif i == 3 and dic[i]:
            dic[i] -= 1
            if curSum >= 0:
                recursion(k + 1, N, curSum//Lst[k])
            else:
                curSum2 = abs(curSum)//Lst[k]
                recursion(k+1,N,-curSum2)
            dic[i] += 1


N = int(input())
dic = {
    0:0,
    1:0,
    2:0,
    3:0
}
maximum = -1e10
minimum = 1e10
Lst = list(map(int,input().split()))
lst = list(map(int,input().split()))
# print(lst)
# print(dic)
for idx in range(4):
    dic[idx] = lst[idx]

recursion(1,N,Lst[0])

print(maximum)
print(minimum)





