# BOJ_2193 이친수
import sys
input = sys.stdin.readline

lst = [0]*91
lst[1] = 1
lst[2] = 1
for i in range(3,91):
    lst[i] = lst[i-1]+lst[i-2]

print(lst[int(input())])





