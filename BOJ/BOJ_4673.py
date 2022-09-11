# BOJ_4673 셀프 넘버 함수

def d(n):
    result = n
    n = str(n)
    for ele in n:
        result += int(ele)
    return result

lst = [x for x in range(1,10001)]
d_lst = []
for i in range(1,10000):
    d_lst.append(d(i))

lst = sorted(list(set(lst) - set(d_lst)))
for ls in lst:
    print(ls)
