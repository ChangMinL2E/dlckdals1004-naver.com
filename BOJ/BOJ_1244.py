# BOJ_1244 스위치 켜고 끄기

def man(n):
    num = len(lst)//n
    for i in range(1,num+1):
        if lst[n*i-1] == 0:
            lst[n*i-1] = 1
        else:
            lst[n*i-1] = 0

def girl(l):
    l = l-1
    st = l
    ed = l+1
    j = 0
    while (l-j >= 0) and (l+j <= len(lst)-1) and (lst[l-j] == lst[l+j]):
        st = l-j
        ed = l+j+1
        j += 1

    for k in range(st,ed):
        if lst[k] == 1:
            lst[k] = 0
        else:
            lst[k] = 1

input()
lst = list(map(int,input().split())) # switch
cnt = int(input())

for _ in range(cnt):
    gen, number = map(int,input().split())
    if gen == 1:
        man(number)
    else:
        girl(number)

for i in range(1,len(lst)+1):
    print(lst[i-1], end= ' ')
    if i%20 == 0:
        print()
# print(*lst)




