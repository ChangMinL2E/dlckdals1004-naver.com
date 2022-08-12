import sys
sys.stdin = open('1221.txt')

T = int(input())

for tc in range(1,T+1):
    N = input().split()
    print(N[0])
    lst = list(input().split())
    lsts = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dic = {}

    for key in lsts:
        dic[key] = 0

    for ls in lst:
        for key in dic:
            if ls == key:
                dic[key] += 1

    for key in dic:
        for i in range(dic[key]):
            print(key, end= " ")
    print()




