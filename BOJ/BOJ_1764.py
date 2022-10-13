# BOK_1764 듣보잡

N,M = map(int,input().split())
lst1 = set([input() for _ in range(N)])
lst2 = set([input() for _ in range(M)])


total = 0
total_lst = sorted(list(set(lst1&lst2)))
# i_k, j_k = 0,0
# for i in range(N):
#     for j in range(M):
#         if i_k<=i and j_k<=j and lst1[i] == lst2[j]:
#             i_k = i
#             j_k = j
#             total += 1
#             total_lst.append(lst1[i])

print(len(total_lst))
for ls in total_lst:
    print(ls)


