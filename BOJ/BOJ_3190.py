# BOJ_3190 뱀
from collections import  deque
import sys
input = sys.stdin.readline

N = int(input())
lst = []
apples = [[0]*N for _ in range(N)]
for _ in range(int(input())):
    row, col = map(int,input().split())
    # lst.append((row-1,col-1))
    apples[row-1][col-1] += 1

trans_direct = []
for _ in range(int(input())):
    trans_direct.append(input().split())

Queue = deque([(0,0)])
dic = [(0,1),(1,0),(0,-1),(-1,0)]

i = 0
dic_i = 0
cnt = 1
while True:
    if i < len(trans_direct): # 아직도 방향전환할 방향이 있다면,
        trans_i = int(trans_direct[i][0])

    x,y = Queue[0][0]+dic[dic_i%4][0], Queue[0][1]+dic[dic_i%4][1]
    if not ((0<=x<N and 0<=y<N) and (not (x,y) in Queue)):# and (x,y) != Queue[-1]) ): # 끝날 조건
        break
    elif apples[x][y]: # 사과가 있다면,
        Queue.appendleft((x,y))
        apples[x][y] -= 1
    else: # 사과가 없다면,
        Queue.appendleft((x,y))
        Queue.pop()


    if i < len(trans_direct) and cnt == trans_i: # 방향전환 해야한다면,
        if trans_direct[i][1] == 'D': # 오른쪽이라면,
            dic_i += 1
        else: # 왼쪽이면,
            dic_i -= 1
        i += 1
    cnt += 1

print(cnt)







