# BOJ_2775 부녀회장

lst = [[x for x in range(1,15)]]
for _ in range(14):
    new_lst = []
    for idx in range(14):
        new_lst.append(sum(lst[-1][0:idx+1]))
    lst.append(new_lst)

# print(lst)

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    print(lst[k][n-1])