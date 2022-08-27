# BOJ_2628 종이자르기

x_lst = [0]
y_lst = [0]

x, y = map(int,input().split())
x_lst.append(x)
y_lst.append(y)

T = int(input())

for _ in range(T):
    axis, value = map(int,input().split())
    if axis == 1:
        x_lst.append(value)
    else:
        y_lst.append(value)

x_lst.sort()
y_lst.sort()

maximum = 0

for i in range(1,len(x_lst)):
    for j in range(1,len(y_lst)):
        temp = (x_lst[i] - x_lst[i-1]) * (y_lst[j] - y_lst[j-1])
        if maximum < temp:
            maximum = temp


print(maximum)