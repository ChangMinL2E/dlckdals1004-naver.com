# BOJ_14503 로봇 청소기
import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
r,c,direct = map(int,input().split())
direct_dic = {
    0:(-1,0),
    1:(0,-1),
    2:(1,0),
    3:(0,1)
}
visited = [list(map(int,input().split())) for _ in range(N)]
# print(visited)
if direct % 2:
    direct = (direct + 2) % 4
Queue = deque([(r,c,direct)])
cnt = 1
visited[r][c] = 2
while Queue:
    cml = True
    q = Queue.popleft()
    r,c,i = q[0],q[1],q[2]
    new_i = i+1
    while 5-(new_i-i):
        x,y = r+direct_dic[new_i%4][0], c+direct_dic[new_i%4][1]
        if 0<=x<N and 0<=y<M and not visited[x][y]:
            visited[x][y] = 2
            Queue.append((x,y,new_i%4))
            cml = False
            cnt += 1
            break
        # 청소 못했으면,
        new_i += 1

    if not cml: # 청소 했으면,
        pass
    else: # cml = True 청소 못했으면,
        x,y = r+direct_dic[(i+2)%4][0], c+direct_dic[(i+2)%4][1]
        if not(0<=x<N) or not (0<=y<M) or visited[x][y] == 1:
            break # 후진시 벽에 부딪히는 경우,
        else:
            Queue.append((x,y,i))

print(cnt)

