# BOJ_14501 퇴사 / DP
from collections import deque

N = int(input())
Lst = [list(map(int,input().split())) for _ in range(N)]

Queue = deque([(0,0)]) # 날짜, 가격

maximum = 0
while Queue:
    q = Queue.popleft()
    if 0<=q[0]<N:
        Queue.append((q[0]+Lst[q[0]][0],q[1]+Lst[q[0]][1]))
        Queue.append((q[0]+1,q[1]))
    elif q[0] == N:
        if maximum < q[1]:
            maximum = q[1]

print(maximum)






