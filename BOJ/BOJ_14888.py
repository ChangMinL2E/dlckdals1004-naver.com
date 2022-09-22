# BOJ_14888 연산자 끼워넣기 / 백트래킹
# 오답

import sys

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
operations = list(map(int,sys.stdin.readline().split())) # 덧셈 뺄셈 곱셈 나눗셈
minimum = 1e+9
maximum = 1e-9

visited = [False]*N

def Backtracking(lst,k,N,curSum,i):
    global minimum, maximum

    if k == N:
        if minimum > curSum:
            minimum = curSum
        if maximum < curSum:
            maximum = curSum
        return

    # for i in range(N): # lst index

    for j in range(4): # operations index
        if j == 0 and operations[j] > 0:
            if not visited[i]:
                visited[i] = True
                operations[j] -= 1
                Backtracking(lst, k+1, N, curSum+lst[i],i+1)
                operations[j] += 1
                visited[i] = False
        elif j == 1 and operations[j] > 0:
            if not visited[i]:
                visited[i] = True
                operations[j] -= 1
                Backtracking(lst, k + 1, N, curSum - lst[i],i+1)
                operations[j] += 1
                visited[i] = False
        elif j == 2 and operations[j] > 0:
            if not visited[i]:
                visited[i] = True
                operations[j] -= 1
                Backtracking(lst, k + 1, N, curSum * lst[i],i+1)
                operations[j] += 1
                visited[i] = False
        elif j == 3 and operations[j] > 0:
            if not visited[i]:
                visited[i] = True
                operations[j] -= 1
                if curSum/lst[i] < 0:
                    # round(abs(curSum/lst[i]))
                    Backtracking(lst, k + 1, N, -(abs(curSum)//abs(lst[i])), i + 1)
                else:
                    Backtracking(lst, k + 1, N, curSum // lst[i],i+1)
                operations[j] += 1
                visited[i] = False

for idx in range(N):
    visited[idx] = True
    Backtracking(lst,1,N,lst[idx],1)
    visited[idx] = False

print(maximum)
print(minimum)