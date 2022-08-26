# BOJ_2309 일곱난쟁이

lst = []
for _ in range(9):
    lst.append(int(input()))

lst.sort()
total = sum(lst)

cml = False
for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
        if total - lst[i] - lst[j] == 100:
            lst.pop(j)
            lst.pop(i)
            cml = True
            break
    if cml:
        break

for ls in lst:
    print(ls)
# print(*lst)
