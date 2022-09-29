# BOJ_1021 덱, 큐
from collections import deque

N, M = map(int,input().split())
pop_lst = list(map(int,input().split()))
pop_Queue = deque()
for p in pop_lst:
    pop_Queue.append(p)

Queue = deque()
for i in range(1,N+1):
    Queue.append(i)

count = 0

while pop_Queue:
    if pop_Queue[0] == Queue[0]:
        pop_Queue.popleft()
        Queue.popleft()

    else:
        idx = Queue.index(pop_Queue[0])
        if idx < len(Queue)-idx:
            while pop_Queue[0] != Queue[0]:
                b = Queue.popleft()
                Queue.append(b)
                count += 1
        else:
            while pop_Queue[0] != Queue[0]:
                b = Queue.pop()
                Queue.appendleft(b)
                count += 1

print(count)
