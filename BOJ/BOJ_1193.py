# BOJ_1193 분수찾기

N = int(input())
lst = [1]
cnt = 1

while True:
    cnt += 1
    lst.append(lst[-1] + cnt)
    if N <= lst[-1]:
        break

if N == 1:
    print('1/1')
else:
    N = lst[-1] - N
    if cnt % 2 == 1:
        print(f'{1 + N}/{cnt - N}')
    else:
        print(f'{cnt - N}/{1 + N}')
