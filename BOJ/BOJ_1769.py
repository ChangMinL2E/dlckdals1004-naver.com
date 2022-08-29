# BOJ_1769 3의 배수

lst = list(map(int,input()))

cml = True
cnt = 0

while cml:
    if len(lst) == 1:
        if lst[0] % 3 == 0:
            print(cnt)
            print('YES')
            cml = False
        else:
            print(cnt)
            print('NO')
            cml = False
    else:
        cnt += 1
        sumLst = sum(lst)
        lst = list(map(int,str(sumLst)))

