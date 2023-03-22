# BOJ_27497 알파벳 블록
from collections import deque

lst = deque()
curIdx = deque()
for t in range(int(input())):
    InputS = input()
    if InputS == '3':
        if len(curIdx) != 0:

            if curIdx[-1] == 0:
                lst.popleft()
                curIdx.pop()
            else:
                lst.pop()
                curIdx.pop()
        else:
            pass
    else:
        A, B = InputS.split()

        if A == '1':
            lst.append(B)
            curIdx.append(1)
        else:
            lst.appendleft(B)
            curIdx.append(0)

if len(lst) == 0:
    print(0)
else:
    print(''.join(lst))
