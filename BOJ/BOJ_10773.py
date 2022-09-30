# BOJ_10773 제로 / 스택

from collections import deque

Stack = deque()
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        Stack.pop()
    else:
        Stack.append(num)

print(sum(Stack))