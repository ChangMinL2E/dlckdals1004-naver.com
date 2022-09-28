# BOJ_1931 Greedy  회의실 방 배정
# 수정중

N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int,input().split())))

lst.sort(key=lambda x:x[1])
# print(lst)
Times = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
while lst:
    i = 0
    idx_lst = []
    for idx in range(len(lst)):
        if idx == 0:
            idx_lst.append(idx)
            Times[cnt][i] = lst[idx]
            i += 1
        elif Times[cnt][i-1][1] <= lst[idx][0]:
            Times[cnt][i] = lst[idx]
            idx_lst.append(idx)
            i += 1
    cnt += 1
    for i in idx_lst[::-1]:
        lst.pop(i)

maximum = 0
for time in Times:
    if maximum < len(time):
        maximum = len(time)

print(maximum)
