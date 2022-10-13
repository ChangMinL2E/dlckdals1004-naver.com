# BOJ_17135 캐슬 디펜스
from itertools import combinations
# from collections import deque
import copy

def dis(A1,A2):
    return abs(A1[0]-A2[0])+abs(A1[1]-A2[1])



N, M, D = map(int,input().split())
Lst = [list(map(int,input().split())) for _ in range(N)]
Archers = list(combinations([x for x in range(M)],3))
total_cnt = 0
maximum = 0
E_lst = []
for row in range(N):
    for col in range(M):
        if Lst[row][col] == 1:
            E_lst.append([row,col])
            total_cnt +=1

E_lst.sort(key=lambda x:x[0])

def simulation(lst,archer):
    global maximum
    cnt = 0
    pass_Cnt = 0

    while total_cnt - cnt - pass_Cnt:

        hit_targets = [-1,-1,-1]
        for i in range(3): # archer
            target_idx = -1
            minimum = 1e10
            for ls_idx in range(len(lst)-1,-1,-1):
                if dis((N,archer[i]),lst[ls_idx]) <= minimum and dis((N,archer[i]),lst[ls_idx]) <= D:
                    if dis((N,archer[i]),lst[ls_idx]) == minimum:
                        if lst[target_idx][1] < lst[ls_idx][1]:
                            pass
                        else:
                            target_idx = ls_idx
                    else:
                        minimum = dis((N,archer[i]),lst[ls_idx])
                        target_idx = ls_idx
            hit_targets[i] = target_idx
        hit_targets = sorted(list(set(hit_targets)))
        for j in hit_targets[::-1]:
            if j != -1:
                lst.pop(j)
                cnt += 1

        for ls_idx in range(len(lst)-1,-1,-1):
            if lst[ls_idx][0] == N - 1:
                lst.pop(ls_idx)
                pass_Cnt += 1
            else:
                lst[ls_idx][0] += 1

        if maximum > total_cnt - pass_Cnt:
            return

    maximum = cnt
    return

for ar in Archers:
    simulation(copy.deepcopy(E_lst),ar)

print(maximum)



