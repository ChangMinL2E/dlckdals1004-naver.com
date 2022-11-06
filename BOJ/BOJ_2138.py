# BOJ_2138
# 전부를 다 보기에는 시간초과.

import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
present1 = list(map(int,list(input().strip())))
Target = list(map(int,list(input().strip())))

present2 = deepcopy(present1)
total1 = 0
total2 = 1
dic = {
    0:1,
    1:0
}

present2[0] = dic[present2[0]]
present2[1] = dic[present2[1]]

idx1 = 1
idx2 = 1
result = -1
while N-idx1:
    if idx1 != N-1:
        if present1[idx1-1] != Target[idx1-1]:
            present1[idx1-1] = dic[present1[idx1-1]]
            present1[idx1] = dic[present1[idx1]]
            present1[idx1+1] = dic[present1[idx1+1]]
            total1 += 1

    else: # idx == N-1
        if present1[idx1-1] != Target[idx1-1]:
            present1[idx1-1] = dic[present1[idx1-1]]
            present1[idx1] = dic[present1[idx1]]
            total1 += 1

    if present1 == Target:
        result = total1
        break

    for i in range(idx1+1,N):
        if present1[i-1] != Target[i-1]:
            idx1 = i
            break
    else:
        idx1 = N


while N - idx2:
    if idx2 != N-1:
        if present2[idx2 - 1] != Target[idx2 - 1]:
            present2[idx2 - 1] = dic[present2[idx2 - 1]]
            present2[idx2] = dic[present2[idx2]]
            present2[idx2 + 1] = dic[present2[idx2 + 1]]
            total2 += 1
    else:
        if present2[idx2 - 1] != Target[idx2 - 1]:
            present2[idx2 - 1] = dic[present2[idx2 - 1]]
            present2[idx2] = dic[present2[idx2]]
            total2 += 1

    if present2 == Target:
        result = total2
        break

    for i in range(idx2 + 1, N):
        if present2[i-1] != Target[i-1]:
            idx2 = i
            break
    else:
        idx2 = N

# if present1 == Target:
#     result = total1
# if present2 == Target:
#     if result == -1:
#         result = total2
#     else:
#         result = min(total1,total2)
print(result)











