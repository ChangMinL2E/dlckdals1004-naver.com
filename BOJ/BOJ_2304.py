# BOJ_2304 창고 다각형

row = int(input())

lst = []
for _ in range(row):
    lst.append(tuple(map(int,input().split())))

lst = sorted(lst, key= lambda x: x[0])

M_idx = 0
for idx in range(len(lst)):
    if lst[M_idx][1] < lst[idx][1]:
        M_idx = idx

l_lst = lst[:M_idx]
r_lst = lst[M_idx+1:]

area = (lst[-1][0] - lst[0][0] +1)*lst[M_idx][1] # 큰 사각형 넓이


L_high = lst[M_idx][1]
R_high = lst[M_idx][1]
L_idx = lst[M_idx][0]
R_idx = lst[M_idx][0]+1

cml = True
while cml:
    M1_idx = 0 # 좌측 최대 인덱스
    if len(l_lst) == 0:
        cml = False
    else:
        for i in range(len(l_lst)):
            if l_lst[M1_idx][1] < l_lst[i][1]:
                M1_idx = i

        area -= (L_idx - l_lst[0][0])*(L_high - l_lst[M1_idx][1]) # 좌측에서 가장 큰 만큼
        L_idx = l_lst[M1_idx][0]
        L_high = l_lst[M1_idx][1]
        l_lst = l_lst[:M1_idx]

cml = True
while cml: # right
    M2_idx = 0  # 좌측 최대 인덱스
    if len(r_lst) == 0:
        cml = False
    else:
        for i in range(len(r_lst)):
            if r_lst[M2_idx][1] < r_lst[i][1]:
                M2_idx = i

        area -= (r_lst[-1][0] - R_idx +1) * (R_high - r_lst[M2_idx][1])  # 좌측에서 가장 큰 만큼
        R_idx = r_lst[M2_idx][0]+1
        R_high = r_lst[M2_idx][1]
        r_lst = r_lst[M2_idx + 1:]

print(area)