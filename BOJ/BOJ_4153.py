# BOJ_4153 직각삼각형 판독
import sys

while True:
    InputS = sys.stdin.readline()

    lst = list(map(int,InputS.split()))
    lst.sort(reverse=True)
    a,b,c = lst[0],lst[1],lst[2]
    if a==0 and b==0 and c==0:
        break

    if a**2 -(b**2+c**2) ==0:
        print('right')
    else:
        print('wrong')



