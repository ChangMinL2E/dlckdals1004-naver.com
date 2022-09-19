lst = [1]
N = int(input())

cnt = 1
while True:
    lst.append(lst[-1]+6*cnt)
    cnt += 1
    if N <= lst[-1]:
        break

if N == 1:
    cnt = 1

print(cnt)