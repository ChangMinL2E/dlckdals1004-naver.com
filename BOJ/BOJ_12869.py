# BOJ_12869 뮤탈리스크
# BFS로 풀어야겠넹..
import sys
input = sys.stdin.readline

def Backtracking(a,b,c,curSum):
    global minimum

    if curSum > minimum:
        return

    if a<=0 and b<=0 and c<=0:
        minimum = curSum
        return

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i!=j and j!=k and k!=i:
                    Backtracking(a-Lst[i],b-Lst[j],c-Lst[k],curSum+1)




N = int(input())
SCV = list(map(int,input().split()))

minimum = 1e10
Lst = [9,3,1]

if len(SCV) == 3:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and k != i:
                    Backtracking(SCV[0] - Lst[i], SCV[1] - Lst[j], SCV[2] - Lst[k],1)
elif len(SCV) == 2:
    SCV.append(0)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and k != i:
                    Backtracking(SCV[0] - Lst[i], SCV[1] - Lst[j], SCV[2] - Lst[k],1)
else:
    minimum = SCV[0]//9+1

print(minimum)




