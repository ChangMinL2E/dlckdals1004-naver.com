# BOJ_2261 가장 가까운 두 점
import sys
input = sys.stdin.readline

minimum = 1e20
def distance(x,y):
    return (x[0]-y[0])**2+(x[1]-y[1])**2

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

for i in range(n-1):
    for j in range(i+1,n):
        if (lst[i][0]-lst[j][0])**2 < minimum and (lst[i][1]-lst[j][1])**2 < minimum:
            if minimum > distance(lst[i],lst[j]):
                minimum = distance(lst[i],lst[j])

print(round(minimum))



