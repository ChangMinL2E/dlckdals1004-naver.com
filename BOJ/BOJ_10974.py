# BOJ_10974 모든 순열 / permutation

def per(lst,k,N):
    if k == N:
        print(*lst)
        return

    for i in range(1,N+1):
        if not visited[i]:
            lst.append(i)
            visited[i] = True
            per(lst,k+1,N)
            visited[i] = False
            lst.pop()

N = int(input())
visited = [False]*(N+1)
for idx in range(1,N+1):
    visited[idx] = True
    per([idx],1,N)
    visited[idx] = False