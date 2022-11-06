# BOJ_10845 큐

import sys
input = sys.stdin.readline
from collections import deque

Queue = deque()

for _ in range(int(input())):
    InputS = input().split()

    if InputS[0] == "pop":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue.popleft())
    elif InputS[0] == 'back':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[-1])
    elif InputS[0] == 'front':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[0])
    elif InputS[0] == "empty":
        if len(Queue) == 0:
            print(1)
        else:
            print(0)
    elif InputS[0] == 'size':
        print(len(Queue))
    else:
        Queue.append(int(InputS[-1]))



