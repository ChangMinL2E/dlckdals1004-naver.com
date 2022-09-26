# BOJ_2164 카드 2 / 덱, 큐

from collections import deque

N = int(input())
lst = deque()
for i in range(1,N+1):
    lst.append(i)

while lst:
    if len(lst)== 1:
        print(lst.popleft())
    else:
        lst.popleft()
        a = lst.popleft()
        lst.append(a)






