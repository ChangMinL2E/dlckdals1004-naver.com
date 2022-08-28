# BOJ_2477_2.py 참외밭 제도전 슈우우웃~!

one_width = int(input())

lst = []
for _ in range(6):
    lst.append(tuple(map(int,input().split())))

x_idx = 0
y_idx = 0
x_maximum = 0
y_maximum = 0

for idx in range(len(lst)):
    if lst[idx][0] == 2 or lst[idx][0] == 1: # 가로 큰 변
        if x_maximum < lst[idx][1]:
            x_maximum = lst[idx][1]
            x_idx = idx
    else: # 세로 큰 변
        if y_maximum < lst[idx][1]:
            y_maximum = lst[idx][1]
            y_idx = idx

width = x_maximum * y_maximum # 큰 사각형의 넓이

if (x_idx == 0 and y_idx == 5) or (x_idx == 5 and y_idx == 0):    # 작은 사각형 넓이
    width -= lst[2][1] * lst[3][1]
else:
    i = max(x_idx,y_idx)
    width -= lst[(i+2)%6][1] * lst[(i+3)%6][1]

width = one_width * width
print(width)