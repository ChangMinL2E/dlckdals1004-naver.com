# BOJ_2477 참외밭

# width_one = int(input())
#
# dic = {}
# for i in range(1,5):
#     dic[i] = []
#
# for _ in range(6): # 데이터 완성
#     Input_lst = list(map(int,input().split()))
#     dic[Input_lst[0]].append(Input_lst[1])
#
# width = 0
# one_lst = []
# two_lst = []
# for idx in dic:
#     if len(dic[idx]) == 1:
#         one_lst.append(idx)
#     else:
#         two_lst.append(idx)
#
# width = 1*dic[one_lst[0]][0]*dic[one_lst[1]][0]
# minus = 1
#
#
# if abs(two_lst[0]-two_lst[1]) == 2:
#     two_lst.sort(reverse=True)
#     minus = minus * dic[two_lst[0]][1]*dic[two_lst[1]][0]
# elif abs(two_lst[0]-two_lst[1]) == 1:
#     two_lst.sort(reverse=False)
#     minus = minus * dic[two_lst[0]][1] * dic[two_lst[1]][0]
# else:
#     two_lst.sort(reverse=True)
#     minus = minus * dic[two_lst[0]][0] * dic[two_lst[1]][1]
#
# width = width_one* (width-minus)
# print(width)

width_one = int(input())

dic = {}
for idx in range(1,5):
    dic[idx] = 0

lst = []
for _ in range(6):
    lst.append(tuple(map(int,input().split())))

for tu in lst:
    dic[tu[0]] += 1

width = 1
minus = 1

two_lst = [] # 두번
one_lst = [] # 한번
for key in dic:
    if dic[key] == 1:
        one_lst.append(key)
    else:
        two_lst.append(key)

for ls in lst:
    if ls[0] in one_lst:
        width *= ls[1]

lst.append(lst[0])
lst.append(lst[1])

# for i in range(1,len(lst)):
#     if lst[i-1][0], lst[i][0] == 3,2:
#         minus = minus*lst[i-1][1]* lst[i][1]
#         break
#     elif lst[i-1][0], lst[i][0] == 2,4:
#         minus = minus * lst[i - 1][1] * lst[i][1]
#         break
#     elif lst[i-1][0], lst[i][0] == 1,3:
#         minus = minus * lst[i - 1][1] * lst[i][1]
#         break
#     elif lst[i-1][0], lst[i][0] == 4,1:
#         minus = minus * lst[i - 1][1] * lst[i][1]
#         break

# width = width_one* (width-minus)
# print(width)

for i in range(1,len(lst)):
    if lst[i-1][0] == 3 and lst[i][0] == 2:
        minus = minus*lst[i-1][1]* lst[i][1]
    elif lst[i-1][0] == 2 and lst[i][0] == 4:
        minus = minus * lst[i - 1][1] * lst[i][1]
    elif lst[i-1][0] == 1 and lst[i][0] == 3:
        minus = minus * lst[i - 1][1] * lst[i][1]
    elif lst[i-1][0] == 4 and lst[i][0] == 1:
        minus = minus * lst[i - 1][1] * lst[i][1]

width = width_one* (width-minus)
print(width)