# BOJ_5430 AC 시간초과
from collections import deque

for tc in range(int(input())):
    actions = input()
    lst_length = int(input())
    lst = list(input()[1:-1].split(','))
    lst = deque(lst)

    if actions.count('D') > lst_length:
        print('error')
    else:
        for i in range(len(actions)):
            if actions[i] == 'R':
                lst.reverse()
            else:
                lst.popleft()
        
        print('['+','.join(lst)+']')
                