# BOJ_10158. 개미

x, y = map(int, input().split())
a, b = map(int, input().split())
count = int(input())

button_x = 1
button_y = 1
x1 = count - (count//(2*x))*(2*x)
y1 = count - (count//(2*y))*(2*y)

while x1:
    if button_x:
        if (x - a) < x1:
            x1 = x1 - (x - a)
            a = x
            button_x = 0
        else:
            a = a + x1
            x1 = 0

    if not button_x:
        if a < x1:
            x1 = x1 - a
            a = 0
            button_x = 1
        else:
            a = a - x1
            x1 = 0


while y1:
    if button_y:
        if (y - b) < y1:
            y1 = y1 - (y - b)
            b = y
            button_y = 0
        else:
            b = b + y1
            y1 = 0

    elif not button_y:
        if b < y1:
            y1 = y1 - b
            b = 0
            button_y = 1
        else:
            b = b - y1
            y1 = 0

print(a, b)




















# cnt_x = 1
# cnt_y = 1
#
# for _ in range(count):
#     if a == x:
#         cnt_x = -1
#     elif a == 0:
#         cnt_x = 1
#
#     if b == y:
#         cnt_y = -1
#     elif b == 0:
#         cnt_y = 1
#
#     a, b = a+cnt_x, b+cnt_y
#
# print(a , b)




