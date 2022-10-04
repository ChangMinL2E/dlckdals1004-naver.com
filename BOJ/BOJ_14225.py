# BOJ_14225 부분순열의 합

def per(k,N,curSum):
    if k == N:
        visited[curSum] = True
        return

    per(k+1,N,curSum+lst[k])
    per(k+1,N,curSum)

N = int(input())
lst = list(map(int,input().split()))
visited = [False]*2000000

per(0,N,0)

print(visited.index(False))