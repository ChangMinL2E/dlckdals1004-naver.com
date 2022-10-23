# BOJ_12852 1로 만들기 2

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
Queue = deque([[N]])

while Queue:
    q = Queue.popleft()
    target = q[-1]
    if q[-1] == 1:
        print(len(q)-1)
        print(*q)
        break

    if q[-1] >= 2:
        if not target % 3:
            q.append(q[-1]//3)
            Queue.append(q[:])
            q.pop()

        if not target % 2:
            q.append(q[-1]//2)
            Queue.append(q[:])
            q.pop()

        q.append(q[-1]-1)
        Queue.append(q)





