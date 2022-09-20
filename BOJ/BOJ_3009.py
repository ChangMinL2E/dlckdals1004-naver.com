# BOJ_3009 네 번째 점(직사각형)

x_lst = []
y_lst = []
for _ in range(3):
    x,y = map(int,input().split())
    x_lst.append(x)
    y_lst.append(y)

for x1 in x_lst:
    if x_lst.count(x1) == 1:
        new_x = x1
for y1 in y_lst:
    if y_lst.count(y1) == 1:
        new_y = y1

print(new_x, new_y)


