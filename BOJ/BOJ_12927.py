# BOJ_12927 배수 스위치

lst = list(input())
lst.insert(0,0)

cnt = 0
sub_cnt = 0

for i in range(1, len(lst)):
    if lst[i] == 'Y':
        cnt += 1
        for j in range(i, len(lst), i):
            if lst[j] == 'Y':
                lst[j] = 'N'
            else:
                lst[j] = 'Y'

print(cnt)