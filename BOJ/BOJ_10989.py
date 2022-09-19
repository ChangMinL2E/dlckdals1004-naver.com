# BOJ_10989 수 정렬하기 3

# 메모리 초과를 방지하기 위해 input() 대신 sys.stdin.readiline()으로 대체.
import sys

N = int(input())

count_lst = [0]*10001

for _ in range(N):
    i = int(sys.stdin.readline())
    count_lst[i] += 1

for idx in range(10001):
    # if count_lst[idx] != 0:
    for _ in range(count_lst[idx]):
        print(idx)