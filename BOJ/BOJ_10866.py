# BOJ_10866 덱

import sys
input = sys.stdin.readline
from collections import deque

Queue = deque()

for _ in range(int(input())):
    InputS = input().split()

    if InputS[0] == "pop_front":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue.popleft())
    elif InputS[0] == "pop_back":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue.pop())
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
    elif InputS[0] == 'push_front':
        Queue.appendleft(int(InputS[-1]))
    else:
        Queue.append(int(InputS[-1]))




