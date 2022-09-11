# BOJ_2108 정렬 통계학
# 시간 초과

lst = []
for _ in range(int(input())):
    lst.append(float(input()))
lst.sort()

dic = {}
lst_set = set(lst)
for key in lst_set:
    dic[key] = 0

A = round(sum(lst)/len(lst))
B = lst[len(lst)//2]
D = abs(lst[-1]-lst[0])

max_cnt = 0
for ls in lst_set:
    if max_cnt<lst.count(ls):
        max_cnt = lst.count(ls)

most_lst = []
for ls in lst_set:
    if lst.count(ls) == max_cnt:
        most_lst.append(ls)
most_lst.sort()

if len(most_lst) == 1:
    C = most_lst[0]
else:
    C = most_lst[1]

P_lst = [A, int(B), int(C), int(D)]
for ele in P_lst:
    print(ele)






