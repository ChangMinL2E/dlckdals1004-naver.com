# BOJ_11055 가장 큰 증가 부분 수열
# 이것도 냅색같이 풀어 제껴야되네

import sys
input = sys.stdin.readline

N = int(input())
Lst = list(map(int,input().split()))

total = [0]*N
total[0] = Lst[0]

for i in range(1,N):
    for j in range(i):
        if Lst[j] < Lst[i]:
            total[i] = max(total[j]+Lst[i],total[i]) # 처음부터 확인하면서 가능한 값이랑 비교
        else: # 수열이 안되면 말이여
            total[i] = max(Lst[i],total[i])
print(max(total))





