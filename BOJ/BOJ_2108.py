# BOJ_2108 정렬 통계학
# 또 시간 초과
N = int(input())
lst = []
dic = {}
total = 0

maximum = 0
most_lst = []

for _ in range(N):
    inputN = int(input())
    if inputN not in lst:
        dic[inputN] = 1
    else:
        dic[inputN] += 1

    if maximum < dic[inputN]:
        maximum = dic[inputN]
        most_lst = [inputN]
    elif maximum == dic[inputN]:
        most_lst.append(inputN)

    total += inputN
    lst.append(inputN)

lst.sort()

A = round(total/N)
B = lst[N//2]
D = lst[-1]-lst[0]
lst = sorted(list(set(lst)))

most_lst.sort()
if len(most_lst) == 1:
    out = most_lst[0]
else:
    out = most_lst[1]

# out = 0
# cnt = 0
# for ls in lst:
#     if maximum == dic[ls]:
#         out = ls
#         cnt += 1
#         if cnt == 2:
#             break

#
# if len(most_lst) == 1:
#     C = most_lst[0]
# else:
#     C = most_lst[1]

print(A)
print(B)
# print(C)
print(out)
print(D)






