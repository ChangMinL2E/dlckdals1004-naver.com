# Swea 2383 점심 식시시간

from collections import deque
from copy import deepcopy
def distance(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def recursion(lst,k,N1):
    global Count

    if k == N1+1:
        cnt = 0
        people1, people2 = [],[]
        stair1,stair2 = deque([]),deque([])
        # 대기 인원을 따로 만들어 줘야 겠다.
        dg1, dg2 = 0,0

        for idx in range(len(Peoples)):
            if not lst[idx]: # 첫번째로 갈꺼면,
                people1.append(distance(Peoples[idx],Stairs[0]))
            else: # 두번째 계단으로 갈꺼면,
                people2.append(distance(Peoples[idx],Stairs[1]))

        people1.sort(reverse=True)
        people2.sort(reverse=True)

        while people1 or people2 or stair1 or stair2 or dg1 or dg2:
            if cnt > Count:
                return

            if 3 != len(stair1):
                while dg1 != 0 and 3 != len(stair1):
                    stair1.appendleft(0)
                    dg1 -= 1

            if 3 != len(stair2):
                while dg2 != 0 and 3 != len(stair2):
                    stair2.appendleft(0)
                    dg2 -= 1
            cnt += 1
            if len(stair1):
                for idx in range(len(stair1)-1,-1,-1):
                    stair1[idx] += 1
                    if stair1[idx] >= len1:
                        stair1.pop()
                    # else:
                    #     break

            if len(stair2):
                for idx in range(len(stair2) - 1, -1, -1):
                    stair2[idx] += 1
                    if stair2[idx] >= len2:
                        stair2.pop()
                    # else:
                    #     break

            if len(stair2):
                for st in stair2:
                    st += 1

            if len(people1):
                for i in range(len(people1)-1,-1,-1):
                    if cnt >= people1[i] and len(stair1) < len1: # 갈수있고, 계단에 사람 꽉 없으면,
                        people1.pop()
                        dg1 += 1
                    else:
                        break

            if len(people2):
                for i in range(len(people2) - 1, -1, -1):
                    if cnt >= people2[i] and len(stair2) < len2:  # 갈수있고, 계단에 사람 꽉 없으면,
                        people2.pop()
                        dg2 += 1
                    else:
                        break
        # print(cnt)
        if Count > cnt:
            Count = cnt

        return

    for i in range(2): # 전체 경우의 수를 보겠다.
        lst.append(i)
        recursion(lst,k+1,N1)
        lst.pop()


for tc in range(1,int(input())+1):
    N = int(input())
    Lst = [list(map(int,input().split())) for _ in range(N)] # 전체적인 map
    Peoples = []
    Stairs = []
    Count = 1e10
    for i in range(N):
        for j in range(N):
            if Lst[i][j] == 1:
                Peoples.append((i,j))
            elif Lst[i][j]: # 1이 아닌 계단이라면,
                Stairs.append((i,j,Lst[i][j])) # 위치와 크기
    # 계단 깊이
    len1,len2 = Stairs[0][2],Stairs[1][2]
    recursion([],1,len(Peoples))
    # recursion([0,0,0,1,1,1],len(Peoples),len(Peoples))
    print(f'#{tc} {Count+1}')



