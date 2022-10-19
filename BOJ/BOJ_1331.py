# BOJ_1331 Night_Tour
from collections import  deque
import sys
input = sys.stdin.readline

dic = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6
}

delta = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

target = list(input())
target[0] = dic[target[0]]
target[1] = int(target[1])
Queue = deque([target])

num = 35
print_result = 'Invalid'
visited = [[False]*(7) for _ in range(7)]
total_cnt = 1
visited[target[0]][target[1]] = True
cml = True
while num:
    num -= 1
    q = Queue.popleft()
    target2 = list(input())
    target2[0] = dic[target2[0]]
    target2[1] = int(target2[1])

    result = 0
    for dt in delta:
        x,y = q[0]+dt[0], q[1]+dt[1]
        if 1<=x<=6 and 1<=y<=6 and x==target2[0] and y==target2[1]:
            result = 1
            Queue.append(target2)
            if not visited[x][y]:
                visited[x][y] = True
                total_cnt+=1
            else:
                print_result = 'Invalid'
            break

    if not result:
        print_result = 'Invalid'
        break
    if num == 0:
        for dt in delta:
            x,y = target2[0]+dt[0], target2[1]+dt[1]
            if x == target[0] and y == target[1]:
                print_result = 'Valid'

while num:
    num -= 1
    input()

if total_cnt != 36:
    print_result = 'Invalid'




print(print_result)




