# BOJ_17626 Four Squares

def recursion(number,cnt):
    global minimum_cnt

    if minimum_cnt < cnt:
        return

    if number == 0:
        minimum_cnt = cnt
        return

    for num in range(int(number**(1/2)),-1,-1):
        if number - square_lst[num] >=0:
            recursion(number-square_lst[num],cnt+1)



N = int(input())

n = 50000**(1/2) # 223.6

square_lst = [x**2 for x in range(1,224)]
square_lst.sort()
# print(square_lst)
minimum_cnt = 1e10

for idx in range(222,-1,-1):
    if N - square_lst[idx] >= 0:
        recursion(N-square_lst[idx],1)

print(minimum_cnt)









