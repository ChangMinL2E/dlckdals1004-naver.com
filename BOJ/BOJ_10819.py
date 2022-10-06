# BOJ_10819 차이를 최대로

def sol(lst):
    total = 0
    for i in range(N-1):
        total += abs(lst[i]-lst[i+1])
    return total

def per(lst,k,N):
    global minimum,maximum

    if k == N:
        score = sol(lst)
        if maximum < score:
            maximum = score
        if minimum > score:
            minimum = score
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            lst.append(Lst[i])
            per(lst,k+1,N)
            lst.pop()
            visited[i] = False

N = int(input())
Lst = list(map(int,input().split()))
maximum = -1e10
minimum = 1e10
visited = [False]*N

for idx in range(N):
    visited[idx] = True
    per([Lst[idx]],1,N)
    visited[idx] = False

print(maximum)


