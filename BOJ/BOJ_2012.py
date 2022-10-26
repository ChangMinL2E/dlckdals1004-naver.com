# BOJ_2012 등수 매기기  
import sys
input = sys.stdin.readline
total = 0
N = int(input())

Lst = []
for _ in range(N):
    Lst.append(int(input()))

Lst.sort()

for i in range(1,N+1):
    total += abs(i-Lst[i-1])
print(total)