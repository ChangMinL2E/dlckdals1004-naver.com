# BOJ_10815  숫자 카드
import sys

N = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

dic = {}
for i in range(-10000000,10000001):
    dic[i] = 0

for ls in lst:
    dic[ls] = 1

for ele in lst:
    if dic[ele]:
        print(1, end=' ')
    else:
        print(0, end=' ')




